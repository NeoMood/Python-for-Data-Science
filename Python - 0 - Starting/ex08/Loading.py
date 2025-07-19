import time
import os
import sys
from time import sleep


def format_time(secs):
    """
        Converts seconds to MM:SS format
    """
    mins, secs = divmod(int(secs), 60)
    return f"{mins:02d}:{secs:02d}"


def ft_tqdm(lst: range) -> None:
    """
    Custom implementation of tqdm-like progress bar for a range.
    Yields each element in the range while displaying a progress bar.
    Args:
        lst (range): The range to iterate over.
    Yields:
        int: The next element in the range.
    """
    try:
        total = len(lst)
        terminal_width = os.get_terminal_size().columns
        reserved_space = 34 + len(f"{total}/{total}")
        available_width = terminal_width - reserved_space
        bar_length = max(10, available_width)
        start_time = time.time()
        for i, elem in enumerate(lst, 1):
            try:
                assert total > 0, "an error occurred"
                percent = int(i / total * 100)
                filled_length = int(bar_length * i // total)
                bar = '█' * filled_length + '░' * (bar_length - filled_length)
                elapsed = time.time() - start_time
                speed = i / elapsed if elapsed > 0 else 0
                remaining = (total - i) / speed if speed > 0 else 0
                elapsed_str = format_time(elapsed)
                remaining_str = format_time(remaining)
                speed_str = f"{speed:6.2f}it/s"
                time_info = f"[{elapsed_str}<{remaining_str}, {speed_str}]"
                print(
                    f"\r{percent:3d}%|{bar}| {i}/{total} {time_info}",
                    end='', flush=True
                )
                yield elem
            except AssertionError as e:
                print(f"AssertionError: {e}")
                sys.exit(1)
        print()
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)


def main():
    try:
        assert len(sys.argv) == 1, "the arguments are bad"
        for _ in ft_tqdm(range(666)):
            sleep(0.005)
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
