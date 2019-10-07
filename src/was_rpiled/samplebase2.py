# modified 2019.10.07 by jrkim
# 기존 samplebase2.py 수정본
# config.ini 를 값을 바탕으로 led option 들을 기본값으로 할당하고 그 뒤에 외부 Arguments 를 허용하도록 변경
import argparse
import time
import sys
import os

import configparser     # config.ini 용

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/..'))
from rgbmatrix import RGBMatrix, RGBMatrixOptions


class Const(object):
    # constants
    INI_FILE_NAME = './config.ini'
    INI_LED_SECTION = 'LED_OPTIONS'
    LED_ROWS = 'led-rows'
    LED_COLS = 'led-cols'
    LED_CHAIN = 'led-chain'
    LED_PARALLEL = 'led-parallel'
    LED_PWM_BITS = 'led-pwm-bits'
    LED_BRIGHTNESS = 'led-brightness'
    LED_GPIO_MAPPING = 'led-gpio-mapping'
    LED_SCAN_MODE = 'led-scan-mode'
    LED_PWM_LSB_NANOSECONDS = 'led-pwm-lsb-nanoseconds'
    LED_SHOW_REFRESH = 'led-show-refresh'
    LED_SLOWDOWN_GPIO = 'led-slowdown-gpio'
    LED_NO_HARDWARE_PULSE = 'led-no-hardware-pulse'
    LED_RGB_SEQUENCE = 'led-rgb-sequence'
    LED_PIXEL_MAPPER = 'led-pixel-mapper'
    LED_ROW_ADDR_TYPE = 'led-row-addr-type'
    LED_MULTIPLEXING = 'led-multiplexing'


class SampleBase2(object):

    def __init__(self, *args, **kwargs):

        self.load_config()      # load config.ini

        self.parser = argparse.ArgumentParser()

        self.parser.add_argument("-r", "--led-rows", action="store", help="Display rows. 16 for 16x32, 32 for 32x32. Default: 32",
                                 default=int(self.LedRows) if 'LedRows' in self.__dict__ else 32, type=int)
        self.parser.add_argument("--led-cols", action="store", help="Panel columns. Typically 32 or 64. (Default: 32)"
                                 , default=int(self.LedCols) if 'LedCols' in self.__dict__ else 32, type=int)
        self.parser.add_argument("-c", "--led-chain", action="store", help="Daisy-chained boards. Default: 1."
                                 , default=int(self.LedChain) if 'LedChain' in self.__dict__ else 1, type=int)
        self.parser.add_argument("-P", "--led-parallel", action="store", help="For Plus-models or RPi2: parallel chains. 1..3. Default: 1"
                                 , default=int(self.LedParallel) if 'LedParallel' in self.__dict__ else 1, type=int)
        self.parser.add_argument("-p", "--led-pwm-bits", action="store", help="Bits used for PWM. Something between 1..11. Default: 11"
                                 , default=int(self.LedPwmBits) if 'LedPwmBits' in self.__dict__ else 11, type=int)
        self.parser.add_argument("-b", "--led-brightness", action="store", help="Sets brightness level. Default: 100. Range: 1..100"
                                 , default=int(self.LedBrightness) if 'LedBrightness' in self.__dict__ else 100, type=int)

        if 'LedGpioMapping' in self.__dict__:
            self.parser.add_argument("-m", "--led-gpio-mapping", help="Hardware Mapping: regular, adafruit-hat, adafruit-hat-pwm"
                                 , default=self.LedGpioMapping, choices=['regular', 'adafruit-hat', 'adafruit-hat-pwm'], type=str)
        else:
            self.parser.add_argument("-m", "--led-gpio-mapping", help="Hardware Mapping: regular, adafruit-hat, adafruit-hat-pwm", choices=['regular', 'adafruit-hat', 'adafruit-hat-pwm'], type=str)

        self.parser.add_argument("--led-scan-mode", action="store", help="Progressive or interlaced scan. 0 Progressive, 1 Interlaced (default)"
                                 , default=int(self.LedScanMode) if 'LedScanMode' in self.__dict__ else 1, choices=range(2), type=int)
        self.parser.add_argument("--led-pwm-lsb-nanoseconds", action="store", help="Base time-unit for the on-time in the lowest significant bit in nanoseconds. Default: 130"
                                 , default=int(self.LedPwmLsbNanoseconds) if 'LedPwmLsbNanoseconds' in self.__dict__ else 130, type=int)

        if 'LedShowRefresh' in self.__dict__:
            self.parser.add_argument("--led-show-refresh", action="store_true", help="Shows the current refresh rate of the LED panel", default=bool(self.LedShowRefresh))
        else:
            self.parser.add_argument("--led-show-refresh", action="store_true", help="Shows the current refresh rate of the LED panel")

        if 'LedSlowdownGpio' in self.__dict__:
            self.parser.add_argument("--led-slowdown-gpio", action="store", help="Slow down writing to GPIO. Range: 1..100. Default: 1"
                                     , default=self.LedSlowdownGpio, choices=range(3), type=int)
        else:
            self.parser.add_argument("--led-slowdown-gpio", action="store", help="Slow down writing to GPIO. Range: 1..100. Default: 1", choices=range(3), type=int)

        if 'LedNoHardwarePulse' in self.__dict__:
            self.parser.add_argument("--led-no-hardware-pulse", action="store", help="Don't use hardware pin-pulse generation", default=bool(self.LedNoHardwarePulse), type=bool)
        else:
            self.parser.add_argument("--led-no-hardware-pulse", action="store", help="Don't use hardware pin-pulse generation")

        self.parser.add_argument("--led-rgb-sequence", action="store", help="Switch if your matrix has led colors swapped. Default: RGB"
                                 , default=self.LedRgbSequence if 'LedRgbSequence' in self.__dict__ else "RGB", type=str)

        self.parser.add_argument("--led-pixel-mapper", action="store", help="Apply pixel mappers. e.g \"Rotate:90\""
                                 , default=self.LedPixelMapper if 'LedPixelMapper' in self.__dict__ else "", type=str)

        self.parser.add_argument("--led-row-addr-type", action="store", help="0 = default; 1=AB-addressed panels;2=row direct"
                                 , default=int(self.LedRowAddrType) if 'LedRowAddrType' in self.__dict__ else 0, type=int, choices=[0,1,2])

        self.parser.add_argument("--led-multiplexing", action="store", help="Multiplexing type: 0=direct; 1=strip; 2=checker; 3=spiral; 4=ZStripe; 5=ZnMirrorZStripe; 6=coreman; 7=Kaler2Scan; 8=ZStripeUneven (Default: 0)"
                                 , default=int(self.LedMultiplexing) if 'LedMultiplexing' in self.__dict__ else 0, type=int)

    def load_config(self):
        print('* load_config');

        config = configparser.ConfigParser()
        config.read(Const.INI_FILE_NAME)
        cfg = config[Const.INI_LED_SECTION]
        # print(config[Const.INI_LED_SECTION])

        for cfgkeyname in cfg.keys():
            print(cfgkeyname, cfg[cfgkeyname])

            if cfgkeyname == Const.LED_COLS:
                self.LedCols = cfg[cfgkeyname]
            elif cfgkeyname == Const.LED_ROWS:
                self.LedRows = cfg[cfgkeyname]
            elif cfgkeyname == Const.LED_CHAIN:
                self.LedChain = cfg[cfgkeyname]
            elif cfgkeyname == Const.LED_PARALLEL:
                self.LedParallel = cfg[cfgkeyname]
            elif cfgkeyname == Const.LED_PWM_BITS:
                self.LedPwmBits = cfg[cfgkeyname]
            elif cfgkeyname == Const.LED_BRIGHTNESS:
                self.LedBrightness = cfg[cfgkeyname]
            elif cfgkeyname == Const.LED_GPIO_MAPPING:
                self.LedGpioMapping = cfg[cfgkeyname]
            elif cfgkeyname == Const.LED_SCAN_MODE:
                self.LedScanMode = cfg[cfgkeyname]
            elif cfgkeyname == Const.LED_PWM_LSB_NANOSECONDS:
                self.LedPwmLsbNanoseconds = cfg[cfgkeyname]
            elif cfgkeyname == Const.LED_SHOW_REFRESH:
                self.LedShowRefresh = cfg[cfgkeyname]
            elif cfgkeyname == Const.LED_SLOWDOWN_GPIO:
                self.LedSlowdownGpio = cfg[cfgkeyname]
            elif cfgkeyname == Const.LED_NO_HARDWARE_PULSE:
                self.LedNoHardwarePulse = cfg[cfgkeyname]
            elif cfgkeyname == Const.LED_RGB_SEQUENCE:
                self.LedRgbSequence = cfg[cfgkeyname]
            elif cfgkeyname == Const.LED_PIXEL_MAPPER:
                self.LedPixelMapper = cfg[cfgkeyname]
            elif cfgkeyname == Const.LED_ROW_ADDR_TYPE:
                self.LedRowAddrType = cfg[cfgkeyname]
            elif cfgkeyname == Const.LED_MULTIPLEXING:
                self.LedMultiplexing = cfg[cfgkeyname]

        # print(self.__dict__)

    def usleep(self, value):
        time.sleep(value / 1000000.0)

    def run(self):
        print("Running")

    def process(self):
        self.args = self.parser.parse_args()

        options = RGBMatrixOptions()

        if self.args.led_gpio_mapping != None:
          options.hardware_mapping = self.args.led_gpio_mapping
        options.rows = self.args.led_rows
        options.cols = self.args.led_cols
        options.chain_length = self.args.led_chain
        options.parallel = self.args.led_parallel
        options.row_address_type = self.args.led_row_addr_type
        options.multiplexing = self.args.led_multiplexing
        options.pwm_bits = self.args.led_pwm_bits
        options.brightness = self.args.led_brightness
        options.pwm_lsb_nanoseconds = self.args.led_pwm_lsb_nanoseconds
        options.led_rgb_sequence = self.args.led_rgb_sequence
        options.pixel_mapper_config = self.args.led_pixel_mapper
        if self.args.led_show_refresh:
          options.show_refresh_rate = 1

        if self.args.led_slowdown_gpio != None:
            options.gpio_slowdown = self.args.led_slowdown_gpio
        if self.args.led_no_hardware_pulse:
          options.disable_hardware_pulsing = True

        self.matrix = RGBMatrix(options = options)

        print('* SampleBase2.Process() : args')
        for arg in self.args.__dict__:
            print('  >', arg, self.args.__dict__[arg])

        try:
            # Start loop
            print("Press CTRL-C to stop sample")
            self.run()
        except KeyboardInterrupt:
            print("Exiting\n")
            sys.exit(0)

        return True
