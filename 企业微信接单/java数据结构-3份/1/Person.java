import java.util.Random;

public class Person {
    private int id; // 主关键字
    private String name;
    private int age;
    private String gender;
    private String address;

    private static final Random random = new Random();

    // 构造函数
    public Person(String name, int age, String gender, String address) {
        this.id = Math.abs(random.nextInt()); // 使用随机数作为ID
        this.name = name;
        this.age = age;
        this.gender = gender;
        this.address = address;
    }

    // Getter 和 Setter 方法
    public int getId() { return id; }
    public void setId(int id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public int getAge() { return age; }
    public void setAge(int age) { this.age = age; }
    public String getGender() { return gender; }
    public void setGender(String gender) { this.gender = gender; }
    public String getAddress() { return address; }
    public void setAddress(String address) { this.address = address; }

    @Override
    public String toString() {
        return "Person [id=" + id + ", 姓名=" + name + ", 年龄=" + age + ", 性别=" + gender + ", 地址=" + address + "]";
    }
}