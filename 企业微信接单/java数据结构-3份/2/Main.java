import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Random;

public class Main {
    public static void main(String[] args) {
        List<Entity> entities = new ArrayList<>();
        Random random = new Random();

        // 随机生成10个Entity对象
        for (int i = 0; i < 10; i++) {
            entities.add(new Entity(random.nextInt(100), // id作为主关键字
                    "Name" + i,
                    random.nextInt(50) + 20, // 年龄20-70
                    random.nextDouble() * 10000, // 薪水0-10000
                    "Dept" + (i % 3 + 1))); // 部门
        }

        System.out.println("\n初始数据:");
        printEntities(entities);

        // 排序操作
        System.out.println("\n冒泡排序 (按主关键字id从小到大排序):");
        bubbleSort(entities);
        // 查找操作
        System.out.println("\n冒泡排序：二分查找 (按id查找):");
        binarySearch(entities, entities.get(5).getId()); // 查找成功
        binarySearch(entities, 999); // 查找失败


        System.out.println("\n直接选择排序 (按主关键字id从小到大排序):");
        selectionSort(entities);

        // 查找操作
        System.out.println("\n选择排序：二分查找 (按id查找):");
        binarySearch(entities, entities.get(5).getId()); // 查找成功
        binarySearch(entities, 999); // 查找失败
    }

    // 冒泡排序
    public static void bubbleSort(List<Entity> entities) {
        int n = entities.size();
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (entities.get(j).getId() > entities.get(j + 1).getId()) {
                    Collections.swap(entities, j, j + 1);
                }
            }
            System.out.println("第" + (i + 1) + "趟排序结果: ");
            printEntities(entities);
        }
    }

    // 直接选择排序
    public static void selectionSort(List<Entity> entities) {
        int n = entities.size();
        for (int i = 0; i < n - 1; i++) {
            int minIndex = i;
            for (int j = i + 1; j < n; j++) {
                if (entities.get(j).getId() < entities.get(minIndex).getId()) {
                    minIndex = j;
                }
            }
            Collections.swap(entities, i, minIndex);
            System.out.println("第" + (i + 1) + "趟排序结果: ");
            printEntities(entities);
        }
    }

    // 二分查找
    public static void binarySearch(List<Entity> entities, int key) {
        int left = 0, right = entities.size() - 1;
        int comparisons = 0;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            comparisons++;
            if (entities.get(mid).getId() == key) {
                System.out.println("查找成功: " + entities.get(mid) + ", 比较次数: " + comparisons);
                return;
            } else if (entities.get(mid).getId() < key) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        System.out.println("查找失败, 比较次数: " + comparisons);
    }

    // 打印实体列表
    public static void printEntities(List<Entity> entities) {
        for (Entity entity : entities) {
            System.out.println(entity);
        }
    }
}
