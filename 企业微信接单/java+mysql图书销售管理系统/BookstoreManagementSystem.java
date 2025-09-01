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
            System.out.println("�鼮��ӳɹ���");
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
            System.out.println("��Ӧ����ӳɹ���");
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

            System.out.println("�����ɹ���");
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

            System.out.println("�˻��ɹ���");
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

            System.out.println("���۱���:");
            System.out.println(String.format("%-30s %-15s %-15s", "�鼮����", "��������", "�����ܶ�"));
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
                    System.out.println("��治�㣬����ʧ�ܣ�");
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

                    System.out.println("���۳ɹ���");
                }
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void mainMenu() {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("��ӭʹ��ͼ�����۹���ϵͳ");
            System.out.println("1. ����鼮");
            System.out.println("2. ��ӹ�Ӧ��");
            System.out.println("3. ����");
            System.out.println("4. �˻�");
            System.out.println("5. ����");
            System.out.println("6. ͳ�Ʊ���");
            System.out.println("0. �˳�ϵͳ");
            System.out.print("������ѡ�");
            String choice = scanner.nextLine();

            switch (choice) {
                case "1":
                    System.out.print("�������鼮���⣺");
                    String title = scanner.nextLine();
                    System.out.print("���������ߣ�");
                    String author = scanner.nextLine();
                    System.out.print("������۸�");
                    double price = Double.parseDouble(scanner.nextLine());
                    System.out.print("������������");
                    int stock = Integer.parseInt(scanner.nextLine());
                    addBook(title, author, price, stock);
                    break;
                case "2":
                    System.out.print("�����빩Ӧ�����ƣ�");
                    String name = scanner.nextLine();
                    System.out.print("��������ϵ��ʽ��");
                    String contact = scanner.nextLine();
                    addSupplier(name, contact);
                    break;
                case "3":
                    System.out.print("�������鼮ID��");
                    int bookId = Integer.parseInt(scanner.nextLine());
                    System.out.print("�����빩Ӧ��ID��");
                    int supplierId = Integer.parseInt(scanner.nextLine());
                    System.out.print("���������������");
                    int quantity = Integer.parseInt(scanner.nextLine());
                    addPurchase(bookId, supplierId, quantity);
                    break;
                case "4":
                    System.out.print("�������鼮ID��");
                    bookId = Integer.parseInt(scanner.nextLine());
                    System.out.print("�������˻�������");
                    quantity = Integer.parseInt(scanner.nextLine());
                    addReturn(bookId, quantity);
                    break;
                case "5":
                    System.out.print("�������鼮ID��");
                    bookId = Integer.parseInt(scanner.nextLine());
                    System.out.print("����������������");
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
                    System.out.println("��Чѡ�");
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