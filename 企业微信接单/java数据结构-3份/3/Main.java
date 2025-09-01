
import java.util.*;

public class Main {
    public static void main(String[] args) {
        List<Product> products = new ArrayList<>();
        Random random = new Random();

        // 随机生成10个Product对象
        for (int i = 0; i < 10; i++) {
            products.add(new Product(random.nextInt(100), // productId作为主关键字
                    "Product" + i,
                    random.nextDouble() * 1000, // 价格0-1000
                    random.nextInt(500), // 库存0-500
                    "Category" + (i % 3 + 1))); // 分类
        }

        System.out.println("\n初始数据:");
        printProducts(products);

        // 排序操作
        System.out.println("\n希尔排序 (按主关键字productId从小到大排序):");
        shellSort(products);
// 查找操作
        System.out.println("\n希尔:二分查找 (按productId查找):");
        binarySearch(products, products.get(5).getProductId()); // 查找成功
        binarySearch(products, 999); // 查找失败


        System.out.println("\n快速排序 (按主关键字productId从小到大排序):");
        quickSort(products, 0, products.size() - 1);
        printProducts(products);

        // 查找操作
        System.out.println("\n快速:二分查找 (按productId查找):");
        binarySearch(products, products.get(5).getProductId()); // 查找成功
        binarySearch(products, 999); // 查找失败
    }

    // 希尔排序
    public static void shellSort(List<Product> products) {
        int n = products.size();
        for (int gap = n / 2; gap > 0; gap /= 2) {
            for (int i = gap; i < n; i++) {
                Product temp = products.get(i);
                int j;
                for (j = i; j >= gap && products.get(j - gap).getProductId() > temp.getProductId(); j -= gap) {
                    products.set(j, products.get(j - gap));
                }
                products.set(j, temp);
            }
            System.out.println("当前间隔" + gap + "排序结果:");
            printProducts(products);
        }
    }

    // 快速排序
    public static void quickSort(List<Product> products, int low, int high) {
        if (low < high) {
            int pi = partition(products, low, high);
            quickSort(products, low, pi - 1);
            quickSort(products, pi + 1, high);
        }
    }

    public static int partition(List<Product> products, int low, int high) {
        Product pivot = products.get(high);
        int i = (low - 1);
        for (int j = low; j < high; j++) {
            if (products.get(j).getProductId() <= pivot.getProductId()) {
                i++;
                Collections.swap(products, i, j);
            }
        }
        Collections.swap(products, i + 1, high);
        return i + 1;
    }

    // 二分查找
    public static void binarySearch(List<Product> products, int key) {
        int left = 0, right = products.size() - 1;
        int comparisons = 0;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            comparisons++;
            if (products.get(mid).getProductId() == key) {
                System.out.println("查找成功: " + products.get(mid) + ", 比较次数: " + comparisons);
                return;
            } else if (products.get(mid).getProductId() < key) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        System.out.println("查找失败, 比较次数: " + comparisons);
    }

    // 打印产品列表
    public static void printProducts(List<Product> products) {
        for (Product product : products) {
            System.out.println(product);
        }
    }
}
