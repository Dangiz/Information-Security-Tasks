import crc_task as task1
import stegonagraphy_task as task2

print(task1.get_control_sum('text.txt'))
print(task2.steganograpy_uncode(task2.steganography_task_encode('text.txt', 'container.txt')))

