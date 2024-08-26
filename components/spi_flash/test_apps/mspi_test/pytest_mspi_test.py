# SPDX-FileCopyrightText: 2022-2023 Espressif Systems (Shanghai) CO LTD
# SPDX-License-Identifier: Apache-2.0
import pytest
from pytest_embedded import Dut


# TODO: [ESP32P4] IDF-8985 [ESP32C5] IDF-8715, IDF-10313, [ESP32C61] IDF-9314 IDF-10991
@pytest.mark.temp_skip_ci(targets=['esp32p4', 'esp32c5', 'esp32c61'], reason='esp32p4, esp32c5 support TBD')
@pytest.mark.supported_targets
@pytest.mark.generic
@pytest.mark.parametrize(
    'config',
    [
        'release',
        'special',
    ],
    indirect=True,
)
def test_mspi_bus(dut: Dut) -> None:
    dut.run_all_single_board_cases()


@pytest.mark.esp32s2
@pytest.mark.esp32s3
@pytest.mark.generic
@pytest.mark.parametrize(
    'config',
    [
        'xip_psram',
    ],
    indirect=True,
)
def test_mspi_bus_xip_psram(dut: Dut) -> None:
    dut.run_all_single_board_cases()


@pytest.mark.esp32
@pytest.mark.esp32s2
@pytest.mark.esp32s3
@pytest.mark.generic
@pytest.mark.parametrize(
    'config',
    [
        'psram',
    ],
    indirect=True,
)
def test_mspi_bus_psram(dut: Dut) -> None:
    dut.run_all_single_board_cases()
