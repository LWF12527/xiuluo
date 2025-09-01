
import java.util.List;

public class SortAndSearch {

    // 二分查找算法
    public static int binarySearch(List<Person> list, int key) {
        int low = 0;
        int high = list.size() - 1;

        while (low <= high) {
            int mid = (low + high) >>> 1;
            int midVal = list.get(mid).getId();

            if (midVal < key)
                low = mid + 1;
            else if (midVal > key)
                high = mid - 1;
            else
                return mid; // 键值等于中间元素
        }
        return -(low + 1);  // 键值不存在
    }

    // 直接插入排序
    public static void insertionSort(List<Person> list) {
        for (int i = 1; i < list.size(); i++) {
            Person current = list.get(i);
            int j = i - 1;

            // 将当前元素与已排序序列中的元素进行比较
            while (j >= 0 && list.get(j).getId() > current.getId()) {
                list.set(j + 1, list.get(j));
                j--;
            }
            list.set(j + 1, current);

            // 输出每一趟排序后的结果
            System.out.println("Insertion Sort Pass " + i + ":");
            list.forEach(System.out::println);
        }
    }

    // 冒泡排序
    public static void bubbleSort(List<Person> list) {
        int n = list.size();
        boolean swapped;
        for (int i = 0; i < n - 1; i++) {
            swapped = false;
            for (int j = 0; j < n - 1 - i; j++) {
                if (list.get(j).getId() > list.get(j + 1).getId()) {
                    // 交换元素
                    Person temp = list.get(j);
                    list.set(j, list.get(j + 1));
                    list.set(j + 1, temp);
                    swapped = true;
                }
            }
            // 如果没有发生交换，说明列表已经是有序的
            if (!swapped)
                break;

            // 输出每一趟排序后的结果
            System.out.println("Bubble Sort Pass " + (i + 1) + ":");
            list.forEach(System.out::println);
        }
    }
}