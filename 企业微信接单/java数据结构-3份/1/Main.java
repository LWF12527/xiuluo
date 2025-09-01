import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<Person> personList = new ArrayList<>();

        // 添加10个Person对象到列表
        for (int i = 0; i < 10; i++) {
            personList.add(new Person("姓名" + i, 20 + i, i % 2 == 0 ? "男" : "女", "地址" + i));
        }

        // 打印初始列表
        System.out.println("初始列表：");
        personList.forEach(System.out::println);

        // 排序前打印
        System.out.println("\n排序前：");
        personList.forEach(System.out::println);

//        // 进行插入排序
//        System.out.println("\n执行插入排序：");
//        SortAndSearch.insertionSort(personList);

        // 或者选择冒泡排序
        System.out.println("\n执行冒泡排序：");
        SortAndSearch.bubbleSort(personList);

        // 查找测试
        int searchKey = personList.get(5).getId(); // 选择一个存在的ID
        int index = SortAndSearch.binarySearch(personList, searchKey);
        if (index >= 0) {
            System.out.println("在索引 " + index + " 处找到元素");
        } else {
            System.out.println("未找到，应插入在索引 " + (-index - 1));
        }

        // 查找失败的情况
        int nonExistentKey = 999999; // 假设这个ID不存在
        index = SortAndSearch.binarySearch(personList, nonExistentKey);
        if (index >= 0) {
            System.out.println("在索引 " + index + " 处找到元素");
        } else {
            System.out.println("未找到，应插入在索引 " + (-index - 1));
        }
    }
}