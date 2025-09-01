import java.sql.*;
import java.time.LocalDate;
import java.util.Scanner;

public class BookstoreManagementSystem {
    private static final String DB_URL = "jdbc:mysql://localhost/bookstore";
    private static final String DB_USER = "root";
    private static final String DB_PASSWORD = "123456";

    private Connection conn;
    private Statement stmt;

    public BookstoreManagementSystem() {
        try {
            conn = DriverManager.getConnection(DB_URL, DB_USER, DB_PASSWORD);
            stmt = conn.createStatement();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void addBook(String title, String author, double price, int stock) {
        try {
            String sql = "INSERT INTO books (title, author, price, stock) VALUES (?, ?, ?, ?)";
            PreparedStatement pstmt = conn.prepareStatement(sql);
            pstmt.setString(1, title);
            pstmt.setString(2, author);
            pstmt.setDouble(3, price);
            pstmt.setInt(4, stock);
            pstmt.executeUpdate();
            System.out.println("书籍添加成功！");
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void addSupplier(String name, String contact) {
        try {
            String sql = "INSERT INTO suppliers (name, contact) VALUES (?, ?)";
            PreparedStatement pstmt = conn.prepareStatement(sql);
            pstmt.setString(1, name);
            pstmt.setString(2, contact);
            pstmt.executeUpdate();
            System.out.println("供应商添加成功！");
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void addPurchase(int bookId, int supplierId, int quantity) {
        try {
            LocalDate purchaseDate = LocalDate.now();
            String sql = "INSERT INTO purchases (book_id, supplier_id, quantity, purchase_date) VALUES (?, ?, ?, ?)";
            PreparedStatement pstmt = conn.prepareStatement(sql);
            pstmt.setInt(1, bookId);
            pstmt.setInt(2, supplierId);
            pstmt.setInt(3, quantity);
            pstmt.setDate(4, Date.valueOf(purchaseDate));
            pstmt.executeUpdate();

            sql = "UPDATE books SET stock = stock + ? WHERE id = ?";
            pstmt = conn.prepareStatement(sql);
            pstmt.setInt(1, quantity);
            pstmt.setInt(2, bookId);
            pstmt.executeUpdate();

            System.out.println("进货成功！");
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void addReturn(int bookId, int quantity) {
        try {
            LocalDate returnDate = LocalDate.now();
            String sql = "INSERT INTO returns (book_id, quantity, return_date) VALUES (?, ?, ?)";
            PreparedStatement pstmt = conn.prepareStatement(sql);
            pstmt.setInt(1, bookId);
            pstmt.setInt(2, quantity);
            pstmt.setDate(3, Date.valueOf(returnDate));
            pstmt.executeUpdate();

            sql = "UPDATE books SET stock = stock - ? WHERE id = ?";
            pstmt = conn.prepareStatement(sql);
            pstmt.setInt(1, quantity);
            pstmt.setInt(2, bookId);
            pstmt.executeUpdate();

            System.out.println("退货成功！");
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void getSalesReport() {
        try {
            String sql = "SELECT b.title, SUM(s.quantity) AS total_quantity, SUM(b.price * s.quantity) AS total_amount " +
                    "FROM sales s INNER JOIN books b ON s.book_id = b.id " +
                    "GROUP BY b.title " +
                    "ORDER BY total_amount DESC";
            ResultSet rs = stmt.executeQuery(sql);

            System.out.println("销售报表:");
            System.out.println(String.format("%-30s %-15s %-15s", "书籍标题", "销售总量", "销售总额"));
            while (rs.next()) {
                String title = rs.getString("title");
                int totalQuantity = rs.getInt("total_quantity");
                double totalAmount = rs.getDouble("total_amount");
                System.out.println(String.format("%-30s %-15s %-15s", title, totalQuantity, totalAmount));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void sellBook(int bookId, int quantity) {
        try {
            String sql = "SELECT stock FROM books WHERE id = ?";
            PreparedStatement pstmt = conn.prepareStatement(sql);
            pstmt.setInt(1, bookId);
            ResultSet rs = pstmt.executeQuery();

            if (rs.next()) {
                int stock = rs.getInt("stock");
                if (quantity > stock) {
                    System.out.println("库存不足，销售失败！");
                } else {
                    LocalDate saleDate = LocalDate.now();
                    sql = "INSERT INTO sales (book_id, quantity, sale_date) VALUES (?, ?, ?)";
                    pstmt = conn.prepareStatement(sql);
                    pstmt.setInt(1, bookId);
                    pstmt.setInt(2, quantity);
                    pstmt.setDate(3, Date.valueOf(saleDate));
                    pstmt.executeUpdate();

                    sql = "UPDATE books SET stock = stock - ? WHERE id = ?";
                    pstmt = conn.prepareStatement(sql);
                    pstmt.setInt(1, quantity);
                    pstmt.setInt(2, bookId);
                    pstmt.executeUpdate();

                    System.out.println("销售成功！");
                }
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void mainMenu() {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("欢迎使用图书销售管理系统");
            System.out.println("1. 添加书籍");
            System.out.println("2. 添加供应商");
            System.out.println("3. 进货");
            System.out.println("4. 退货");
            System.out.println("5. 销售");
            System.out.println("6. 统计报表");
            System.out.println("0. 退出系统");
            System.out.print("请输入选项：");
            String choice = scanner.nextLine();

            switch (choice) {
                case "1":
                    System.out.print("请输入书籍标题：");
                    String title = scanner.nextLine();
                    System.out.print("请输入作者：");
                    String author = scanner.nextLine();
                    System.out.print("请输入价格：");
                    double price = Double.parseDouble(scanner.nextLine());
                    System.out.print("请输入库存量：");
                    int stock = Integer.parseInt(scanner.nextLine());
                    addBook(title, author, price, stock);
                    break;
                case "2":
                    System.out.print("请输入供应商名称：");
                    String name = scanner.nextLine();
                    System.out.print("请输入联系方式：");
                    String contact = scanner.nextLine();
                    addSupplier(name, contact);
                    break;
                case "3":
                    System.out.print("请输入书籍ID：");
                    int bookId = Integer.parseInt(scanner.nextLine());
                    System.out.print("请输入供应商ID：");
                    int supplierId = Integer.parseInt(scanner.nextLine());
                    System.out.print("请输入进货数量：");
                    int quantity = Integer.parseInt(scanner.nextLine());
                    addPurchase(bookId, supplierId, quantity);
                    break;
                case "4":
                    System.out.print("请输入书籍ID：");
                    bookId = Integer.parseInt(scanner.nextLine());
                    System.out.print("请输入退货数量：");
                    quantity = Integer.parseInt(scanner.nextLine());
                    addReturn(bookId, quantity);
                    break;
                case "5":
                    System.out.print("请输入书籍ID：");
                    bookId = Integer.parseInt(scanner.nextLine());
                    System.out.print("请输入销售数量：");
                    quantity = Integer.parseInt(scanner.nextLine());
                    sellBook(bookId, quantity);
                    break;
                case "6":
                    getSalesReport();
                    break;
                case "0":
                    scanner.close();
                    closeConnection();
                    return;
                default:
                    System.out.println("无效选项！");
                    break;
            }
        }
    }

    public void closeConnection() {
        try {
            if (stmt != null) {
                stmt.close();
            }
            if (conn != null) {
                conn.close();
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        BookstoreManagementSystem system = new BookstoreManagementSystem();
        system.mainMenu();
    }
}