# -*- coding: utf-8 -*-
import time
import sys

# Set UTF-8 encoding for output
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Lay thong tin ve cac loai clock
print("=== Thong tin cac loai Clock ===\n")

# 1. Monotonic clock
print("1. Monotonic Clock:")
info = time.get_clock_info('monotonic')
print(f"   - Resolution: {info.resolution} seconds")
print(f"   - Adjustable: {info.adjustable}")
print(f"   - Implementation: {info.implementation}")
print()

# 2. Performance counter
print("2. Performance Counter:")
info = time.get_clock_info('perf_counter')
print(f"   - Resolution: {info.resolution} seconds")
print(f"   - Adjustable: {info.adjustable}")
print(f"   - Implementation: {info.implementation}")
print()

# 3. Process time
print("3. Process Time:")
info = time.get_clock_info('process_time')
print(f"   - Resolution: {info.resolution} seconds")
print(f"   - Adjustable: {info.adjustable}")
print(f"   - Implementation: {info.implementation}")
print()

# 4. System time
print("4. System Time:")
info = time.get_clock_info('time')
print(f"   - Resolution: {info.resolution} seconds")
print(f"   - Adjustable: {info.adjustable}")
print(f"   - Implementation: {info.implementation}")
print()

# Xem tat ca thong tin
print("\n=== Tat ca thong tin ===")
for clock_name in ['monotonic', 'perf_counter', 'process_time', 'time', 'thread_time']:
    try:
        info = time.get_clock_info(clock_name)
        print(f"\n{clock_name}:")
        print(f"  {info}")
    except (ValueError, AttributeError):
        print(f"\n{clock_name}: Not available")
