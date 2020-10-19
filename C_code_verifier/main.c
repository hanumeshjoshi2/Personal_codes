/*
 * @file       main.c
 *
 * @brief      TDoA Tag Application
 *
 * @author     Decawave
 *
 * @attention  Copyright 2018 (c) DecaWave Ltd, Dublin, Ireland.
 *             All rights reserved.
 *
 */

#include "port_platform.h"
#include "deca_types.h"
#include "deca_param_types.h"
#include "deca_regs.h"
#include "deca_device_api.h"
#include "default_config.h"
#include "instance.h"
#include "config.h"

#ifndef KX124
#include "LIS2DH12.h"
#else
#include "KX_124_drv.h"
#endif

#ifdef WDT_ENABLE
#include "nrf_drv_wdt.h"
#endif

#ifdef BLE_ENABLE
#include "ble_cus.h"
#endif

#ifdef BATT_GAUGE
#include "STC3117.h"
#endif

#ifdef LPS22HB
#include "lps22hb_interface.h"
#endif

/**< Task delay. Delays a LED0 task for 200 ms */
#define TASK_DELAY      200

/**< Timer period. LED1 timer will expire after 1000 ms */
#define TIMER_PERIOD    2000

#ifdef WDT_ENABLE
nrf_drv_wdt_channel_id m_channel_id;
#endif

/* Configuration in default_config.h */
app_cfg_t app;

float accel_bias[3];
uint16_t ZERO_PDT = 0;
int8_t power_cycle_status_ret = 0;

#ifdef BLE_ENABLE
extern ble_init();
extern idle_state_handle();
#endif

/* @Fn  inittestapplication
 * @brief Function for initializing the SPI.
 *
 * @param[in] void
*/

int inittestapplication(void)


{
    int32_t result = 0;
    int ID = 0; // Decawave Device ID
    decaIrqStatus_t a;

    /* Disable ScenSor (EXT_IRQ) before starting */
    a = decamutexon();
    // Set SPI clock to 2MHz
    port_set_dw1000_slowrate();
    // Read Decawave chip ID
    devID = instancereaddeviceid() ;

    if(DWT_DEVICE_ID != devID)
    {
        //wake up device from low power mode
        //NOTE - in the ARM  code just drop chip select for 200us
        port_wakeup_dw1000();
        // SPI not working or Unsupported Device ID
        devID = instancereaddeviceid() ;
        if (DWT_DEVICE_ID != devID){
            return -1 ;
        }
    }

    // configure: if DW1000 is calibrated then OTP config is used, enable sleep
    result = instance_init( 1 );

    if (0 > result) {
        return(-1) ; // Some failure has occurred
    }
    // Set SPI to 8MHz clock
    port_set_dw1000_fastrate();
    // Read Decawave chip ID
    devID = instancereaddeviceid() ;

    if (DWT_DEVICE_ID != devID)   // Means it is NOT MP device
    {
        // SPI not working or Unsupported Device ID
        return(-1);
    }

    instance_config(app.pConfig) ;  // Set operating channel etc

    decamutexoff(a); //enable SenSor (EXT_IRQ) before starting
    return result;
}

#ifdef WDT_ENABLE
/**
 * @brief WDT events handler.
 */
void wdt_event_handler(void)
{
    //NOTE: The max amount of time we can spend in WDT interrupt is two cycles of 32768[Hz] clock - after that, reset occurs
}
#endif

#ifdef WDT_ENABLE
void wdt_init()
{
    //Configure WDT.
    nrfx_wdt_config_t config = NRF_DRV_WDT_DEAFULT_CONFIG;
    ret_code_t err_code = nrf_drv_wdt_init(&config, wdt_event_handler);
    APP_ERROR_CHECK(err_code);
    err_code = nrf_drv_wdt_channel_alloc(&m_channel_id);
    APP_ERROR_CHECK(err_code);
    nrf_drv_wdt_enable();
}
#endif

int main(void)
{
    char fw_ver[FW_VER_SIZE + 1];
    const int K_A;
#ifdef HW_PP_TAG
    LEDS_CONFIGURE(BSP_LED_0_MASK | BSP_LED_2_MASK | BSP_LED_3_MASK);
    LEDS_OFF(BSP_LED_0_MASK | BSP_LED_2_MASK | BSP_LED_3_MASK);
    // TBD: BSP_LED_1_MASK pin if configured for led then it will consume around 5mA current
#else
    LEDS_CONFIGURE(BSP_LED_0_MASK | BSP_LED_1_MASK | BSP_LED_2_MASK | BSP_LED_3_MASK);
    LEDS_OFF(BSP_LED_0_MASK | BSP_LED_1_MASK | BSP_LED_2_MASK | BSP_LED_3_MASK);
#endif

    memset(&app,0,sizeof(app));
    peripherals_init();

    /* reset decawave */
    reset_DW1000();

    /* set defualt PRF and bit rate etc.. */
    load_bssConfig();/**< load the RAM Configuration parameters from NVM block */
    app.pConfig = get_pbssConfig();

    if(inittestapplication() < 0)
    {
        return -1; // Failed to intialze SPI.
    }

    app.firststart = 1;
    /* Enable blink */
    app.blinkenable = 1;
    app.current_blink_interval_ms = app.pConfig->blink.interval_in_ms;
    
    uint8 eui64[ADDR_BYTE_SIZE] = { 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0xCA, 0xDE};
    uint8_t default_tagID[ADDR_BYTE_SIZE] = {0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08};
    power_cycle_status_ret = memcmp(app.pConfig->tagID, default_tagID, ADDR_BYTE_SIZE);
    // we want exact Address representation in Little- and Big- endian
    uint32 id= ulong2littleEndian(dwt_getpartid());
    memcpy(eui64, &id, sizeof(uint32));
    memcpy(app.pConfig->tagID, eui64, ADDR_BYTE_SIZE);

    sprintf(fw_ver, "%.2d.%.2d.%.2d", FW_VER_MAJOR_NUM, FW_VER_MINOR_NUM, FW_VER_PATCH_NUM);
#ifdef PP_DBG_PRINTF
    NRF_LOG_DEBUG("FW_VER in app = %8s\n", fw_ver);
    NRF_LOG_DEBUG("FW_VER in flash = %8s\n", app.pConfig->app_config.fw_ver);
#endif

    if(memcmp(app.pConfig->app_config.fw_ver, fw_ver, FW_VER_SIZE))
    {
#ifdef PP_DBG_PRINTF
      NRF_LOG_DEBUG("FW_VER compare failed - updating flash.. \n");
#endif
      memcpy(app.pConfig->app_config.fw_ver, fw_ver, FW_VER_SIZE);
      power_cycle_status_ret = 0;
    }
    else
    {
#ifdef PP_DBG_PRINTF
        NRF_LOG_DEBUG("FW_VER compare success\n");
#endif
    }

#ifdef BLE_ENABLE
    ble_init();
#endif
    if(power_cycle_status_ret == 0)
    {
        save_bssConfig(app.pConfig);
    }

#ifdef BLE_ENABLE
    else if(app.pConfig->dev_state == ASSOCIATE_STATE)
    {
        memcpy(app.pConfig->ble_pkt_data.pdt, &ZERO_PDT, BLE_PKT_PDT_SIZE);
        save_bssConfig(app.pConfig);
    }
#endif

#ifdef KX124
    // Initialise the Kionix accelerometer
    KX124_driver_init();
#endif

#ifdef LPS22HB
    init_baro();
#endif

#ifdef LIS2DH12
    uint8_t u8ID;
    // Initialise the accelerometer
    vLIS2_Init(); /* TBD - is it really blocking for 20ms */

    // Check the TWI and acceleromter are talking

    u8ID = u8LIS2_TestRead();

    vLIS2_PowerDown();

    calcaRes(A_SCALE_2G);

    // Set accelerometer activity detection level
    vLIS2_EnableWakeUpDetect();

    // Configure MCU to accept LIS2DH12 INT1 pin interrupts^M
    vLIS2_InterruptInit();

    //lis2dh12_offsetBias(accel_bias);
#endif

#ifdef WDT_ENABLE
    wdt_init();
#endif

#ifdef BATT_GAUGE
    nrf_delay_ms(1000); //TBD: 100ms didnt work for batt gauge read data while run mode. vBatt_getData reurn false. So we put 1sec delay and tested runtime for batt data. It worked.
    vBatt_init();
#endif

    // No RTOS task here so just call the main loop here.
    // Loop forever responding to ranging requests.
    while(1)
    {
#ifdef WDT_ENABLE
         nrf_drv_wdt_feed();
#endif

#ifdef BLE_ENABLE
        idle_state_handle();
#endif
        // checking UART buffer ready to proceed
#ifdef CLI_MODE_ENABLE
        if( deca_uart_rx_data_ready() )
        {
            /* process UART msg based on user input. */
            process_uartmsg();
        }
#endif
        if (app.blinkenable)
        {
            instance_run();    //< transmit packet if allowed
        }
    }
}
