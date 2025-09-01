import java.sql.*;
import java.util.Scanner;

public class BusTicketSystem {
    private static final String DB_URL = "jdbc:mysql://localhost/BUS_mag";
    private static final String DB_USERNAME = "root";
    private static final String DB_PASSWORD = "123456";

    public static void main(String[] args) {
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            Connection conn = DriverManager.getConnection(DB_URL, DB_USERNAME, DB_PASSWORD);
            System.out.println("已连接到数据库");

            Scanner scanner = new Scanner(System.in);

            while (true) {
                System.out.println("欢迎使用公交车票系统");
                System.out.println("1. 用户登录");
                System.out.println("2. 管理员登录");
                System.out.println("3. 退出");
                System.out.print("请输入您的选择：");
                int choice = scanner.nextInt();

                switch (choice) {
                    case 1:
                        userLogin(conn, scanner);
                        break;
                    case 2:
                        adminLogin(conn, scanner);
                        break;
                    case 3:
                        System.out.println("正在退出系统...");
                        conn.close();
                        System.exit(0);
                        break;
                    default:
                        System.out.println("无效的选择，请重试。");
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void userLogin(Connection conn, Scanner scanner) throws SQLException {
        System.out.println("用户登录");
        System.out.print("请输入用户名：");
        String username = scanner.next();
        System.out.print("请输入密码：");
        String password = scanner.next();

        String query = "SELECT * FROM user WHERE username = ? AND password = ?";
        PreparedStatement statement = conn.prepareStatement(query);
        statement.setString(1, username);
        statement.setString(2, password);
        ResultSet resultSet = statement.executeQuery();

        if (resultSet.next()) {
            System.out.println("登录成功");
            int userId = resultSet.getInt("id");
            userMenu(conn, scanner, userId);
        } else {
            System.out.println("无效的用户名或密码");
        }
    }

    private static void userMenu(Connection conn, Scanner scanner, int userId) throws SQLException {
        while (true) {
            System.out.println("用户菜单");
            System.out.println("1. 查看和更新个人信息");
            System.out.println("2. 浏览车辆信息");
            System.out.println("3. 预定车票");
            System.out.println("4. 查看已购车票记录");
            System.out.println("5. 取消购买车票");
            System.out.println("6. 注销");
            System.out.print("请输入您的选择：");
            int choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    viewAndUpdateUserInfo(conn, scanner, userId);
                    break;
                case 2:
                    browseVehicleInfo(conn);
                    break;
                case 3:
                    reserveTicket(conn, scanner, userId);
                    break;
                case 4:
                    viewPurchasedTickets(conn, userId);
                    break;
                case 5:
                    cancelTicket(conn, scanner, userId);
                    break;
                case 6:
                    System.out.println("正在注销...");
                    return;
                default:
                    System.out.println("无效的选择，请重试。");
            }
        }
    }

    private static void viewAndUpdateUserInfo(Connection conn, Scanner scanner, int userId) throws SQLException {
        String query = "SELECT * FROM user WHERE id = ?";
        PreparedStatement statement = conn.prepareStatement(query);
        statement.setInt(1, userId);
        ResultSet resultSet = statement.executeQuery();

        if (resultSet.next()) {
            System.out.println("个人信息");
            System.out.println("用户名：" + resultSet.getString("username"));
            System.out.println("邮箱：" + resultSet.getString("email"));
            System.out.println("电话：" + resultSet.getString("phone"));

            System.out.println("是否要更新您的信息？（Y/N）");
            String choice = scanner.next();

            if (choice.equalsIgnoreCase("Y")) {
                System.out.print("请输入新的邮箱：");
                String newEmail = scanner.next();
                System.out.print("请输入新的电话：");
                String newPhone = scanner.next();

                // 执行更新用户信息的操作
                String updateQuery = "UPDATE user SET email = ?, phone = ? WHERE id = ?";
                PreparedStatement updateStatement = conn.prepareStatement(updateQuery);
                updateStatement.setString(1, newEmail);
                updateStatement.setString(2, newPhone);
                updateStatement.setInt(3, userId);
                int rowsAffected = updateStatement.executeUpdate();

                if (rowsAffected > 0) {
                    System.out.println("个人信息已更新");
                } else {
                    System.out.println("更新个人信息时出现错误");
                }
            }
        }
    }

    private static void browseVehicleInfo(Connection conn) throws SQLException {
        String query = "SELECT * FROM vehicle";
        Statement statement = conn.createStatement();
        ResultSet resultSet = statement.executeQuery(query);

        System.out.println("车辆信息");
        System.out.println("--------------------------------------------------");
        System.out.println("编号\t出发地\t目的地\t出发时间\t\t到达时间\t\t车辆类型\t票价\t最大载客量\t售票情况");
        System.out.println("--------------------------------------------------");

        while (resultSet.next()) {
            int id = resultSet.getInt("id");
            String departure = resultSet.getString("departure");
            String destination = resultSet.getString("destination");
            Timestamp departureTime = resultSet.getTimestamp("departure_time");
            Timestamp arrivalTime = resultSet.getTimestamp("arrival_time");
            String vehicleType = resultSet.getString("vehicle_type");
            double ticketPrice = resultSet.getDouble("ticket_price");
            int maxCapacity = resultSet.getInt("max_capacity");
            int ticketStatus = resultSet.getInt("ticket_status");

            System.out.printf("%d\t%s\t%s\t%s\t%s\t%s\t%.2f\t%d\t%d%n",
                    id, departure, destination, departureTime, arrivalTime, vehicleType, ticketPrice, maxCapacity, ticketStatus);
        }

        System.out.println("--------------------------------------------------");
    }

    private static void reserveTicket(Connection conn, Scanner scanner, int userId) throws SQLException {
        browseVehicleInfo(conn);

        System.out.print("请输入要预定的车辆编号：");
        int vehicleId = scanner.nextInt();

        // 检查车辆是否有余票
        String checkTicketQuery = "SELECT ticket_status FROM vehicle WHERE id = ?";
        PreparedStatement checkTicketStatement = conn.prepareStatement(checkTicketQuery);
        checkTicketStatement.setInt(1, vehicleId);
        ResultSet checkTicketResult = checkTicketStatement.executeQuery();

        if (checkTicketResult.next()) {
            int ticketStatus = checkTicketResult.getInt("ticket_status");

            if (ticketStatus == 0) {
                // 执行预定车票的操作
                String reserveTicketQuery = "INSERT INTO ticket (user_id, vehicle_id, purchase_time) VALUES (?, ?, NOW())";
                PreparedStatement reserveTicketStatement = conn.prepareStatement(reserveTicketQuery);
                reserveTicketStatement.setInt(1, userId);
                reserveTicketStatement.setInt(2, vehicleId);
                int rowsAffected = reserveTicketStatement.executeUpdate();

                if (rowsAffected > 0) {
                    System.out.println("车票预定成功");
                } else {
                    System.out.println("预定车票时出现错误");
                }
            } else {
                System.out.println("该车辆的车票已售罄");
            }
        } else {
            System.out.println("无效的车辆编号");
        }
    }

    private static void viewPurchasedTickets(Connection conn, int userId) throws SQLException {
        String query = "SELECT t.id, v.departure, v.destination, v.departure_time, v.arrival_time, v.vehicle_type, v.ticket_price " +
                "FROM ticket t " +
                "JOIN vehicle v ON t.vehicle_id = v.id " +
                "WHERE t.user_id = ?";
        PreparedStatement statement = conn.prepareStatement(query);
        statement.setInt(1, userId);
        ResultSet resultSet = statement.executeQuery();

        System.out.println("已购车票记录");
        System.out.println("--------------------------------------------------");
        System.out.println("编号\t出发地\t目的地\t出发时间\t\t到达时间\t\t车辆类型\t票价");
        System.out.println("--------------------------------------------------");

        while (resultSet.next()) {
            int ticketId = resultSet.getInt("id");
            String departure = resultSet.getString("departure");
            String destination = resultSet.getString("destination");
            Timestamp departureTime = resultSet.getTimestamp("departure_time");
            Timestamp arrivalTime = resultSet.getTimestamp("arrival_time");
            String vehicleType = resultSet.getString("vehicle_type");
            double ticketPrice = resultSet.getDouble("ticket_price");

            System.out.printf("%d\t%s\t%s\t%s\t%s\t%s\t%.2f%n",
                    ticketId, departure, destination, departureTime, arrivalTime, vehicleType, ticketPrice);
        }

        System.out.println("--------------------------------------------------");
    }

    private static void cancelTicket(Connection conn, Scanner scanner, int userId) throws SQLException {
        viewPurchasedTickets(conn, userId);

        System.out.print("请输入要取消的车票编号：");
        int ticketId = scanner.nextInt();

        // 检查车票是否属于当前用户
        String checkTicketQuery = "SELECT * FROM ticket WHERE id = ? AND user_id = ?";
        PreparedStatement checkTicketStatement = conn.prepareStatement(checkTicketQuery);
        checkTicketStatement.setInt(1, ticketId);
        checkTicketStatement.setInt(2, userId);
        ResultSet checkTicketResult = checkTicketStatement.executeQuery();

        if (checkTicketResult.next()) {
            // 执行取消车票的操作
            String cancelTicketQuery = "DELETE FROM ticket WHERE id = ?";
            PreparedStatement cancelTicketStatement = conn.prepareStatement(cancelTicketQuery);
            cancelTicketStatement.setInt(1, ticketId);
            int rowsAffected = cancelTicketStatement.executeUpdate();

            if (rowsAffected > 0) {
                System.out.println("车票取消成功");
            } else {
                System.out.println("取消车票时出现错误");
            }
        } else {
            System.out.println("无效的车票编号或该车票不属于您");
        }
    }

    private static void adminLogin(Connection conn, Scanner scanner) throws SQLException {
        System.out.println("管理员登录");
        System.out.print("请输入用户名：");
        String username = scanner.next();
        System.out.print("请输入密码：");
        String password = scanner.next();

        String query = "SELECT * FROM admin WHERE username = ? AND password = ?";
        PreparedStatement statement = conn.prepareStatement(query);
        statement.setString(1, username);
        statement.setString(2, password);
        ResultSet resultSet = statement.executeQuery();

        if (resultSet.next()) {
            System.out.println("登录成功");
            adminMenu(conn, scanner);
        } else {
            System.out.println("无效的用户名或密码");
        }
    }

    private static void adminMenu(Connection conn, Scanner scanner) throws SQLException {
        while (true) {
            System.out.println("管理员菜单");
            System.out.println("1. 查看和更新车辆信息");
            System.out.println("2. 查看和更新用户信息");
            System.out.println("3. 查看和更新车票信息");
            System.out.println("4. 返回上级菜单");
            System.out.print("请输入您的选择：");
            int choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    browseAndUpdateVehicleInfo(conn, scanner);
                    break;
                case 2:
                    browseAndUpdateUserInfo(conn, scanner);
                    break;
                case 3:
                    browseAndUpdateTicketInfo(conn, scanner);
                    break;
                case 4:
                    System.out.println("正在返回上级菜单...");
                    return;
                default:
                    System.out.println("无效的选择，请重试。");
            }
        }
    }

    private static void browseAndUpdateVehicleInfo(Connection conn, Scanner scanner) throws SQLException {
        browseVehicleInfo(conn);

        System.out.print("请输入要更新的车辆编号：");
        int vehicleId = scanner.nextInt();

        // 检查车辆是否存在
        String checkVehicleQuery = "SELECT * FROM vehicle WHERE id = ?";
        PreparedStatement checkVehicleStatement = conn.prepareStatement(checkVehicleQuery);
        checkVehicleStatement.setInt(1, vehicleId);
        ResultSet checkVehicleResult = checkVehicleStatement.executeQuery();

        if (checkVehicleResult.next()) {
            System.out.println("车辆信息");
            System.out.println("1. 出发地");
            System.out.println("2. 目的地");
            System.out.println("3. 出发时间");
            System.out.println("4. 预计到达时间");
            System.out.println("5. 车辆类型");
            System.out.println("6. 票价");
            System.out.println("7. 最大载客量");
            System.out.println("8. 售票情况");
            System.out.println("9. 返回上级菜单");
            System.out.print("请输入要更新的信息编号：");
            int infoChoice = scanner.nextInt();

            if (infoChoice >= 1 && infoChoice <= 8) {
                scanner.nextLine(); // Consume the newline character

                System.out.print("请输入新的信息：");
                String newInfo = scanner.nextLine();

                // 执行更新车辆信息的操作
                String updateInfoQuery = "";
                switch (infoChoice) {
                    case 1:
                        updateInfoQuery = "UPDATE vehicle SET departure = ? WHERE id = ?";
                        break;
                    case 2:
                        updateInfoQuery = "UPDATE vehicle SET destination = ? WHERE id = ?";
                        break;
                    case 3:
                        updateInfoQuery = "UPDATE vehicle SET departure_time = ? WHERE id = ?";
                        break;
                    case 4:
                        updateInfoQuery = "UPDATE vehicle SET arrival_time = ? WHERE id = ?";
                        break;
                    case 5:
                        updateInfoQuery = "UPDATE vehicle SET vehicle_type = ? WHERE id = ?";
                        break;
                    case 6:
                        updateInfoQuery = "UPDATE vehicle SET ticket_price = ? WHERE id = ?";
                        break;
                    case 7:
                        updateInfoQuery = "UPDATE vehicle SET max_capacity = ? WHERE id = ?";
                        break;
                    case 8:
                        updateInfoQuery = "UPDATE vehicle SET ticket_status = ? WHERE id = ?";
                        break;
                }

                PreparedStatement updateInfoStatement = conn.prepareStatement(updateInfoQuery);
                updateInfoStatement.setString(1, newInfo);
                updateInfoStatement.setInt(2, vehicleId);
                int rowsAffected = updateInfoStatement.executeUpdate();

                if (rowsAffected > 0) {
                    System.out.println("车辆信息已更新");
                } else {
                    System.out.println("更新车辆信息时出现错误");
                }
            } else if (infoChoice == 9) {
                System.out.println("正在返回上级菜单...");
            } else {
                System.out.println("无效的信息编号");
            }
        } else {
            System.out.println("无效的车辆编号");
        }
    }

    private static void browseAndUpdateUserInfo(Connection conn, Scanner scanner) throws SQLException {
        String query = "SELECT * FROM user";
        Statement statement = conn.createStatement();
        ResultSet resultSet = statement.executeQuery(query);

        System.out.println("用户信息");
        System.out.println("--------------------------------------------------");
        System.out.println("编号\t用户名\t邮箱\t电话");
        System.out.println("--------------------------------------------------");

        while (resultSet.next()) {
            int userId = resultSet.getInt("id");
            String username = resultSet.getString("username");
            String email = resultSet.getString("email");
            String phone = resultSet.getString("phone");

            System.out.printf("%d\t%s\t%s\t%s%n", userId, username, email, phone);
        }

        System.out.println("--------------------------------------------------");

        System.out.print("请输入要更新的用户编号：");
        int userId = scanner.nextInt();

        // 检查用户是否存在
        String checkUserQuery = "SELECT * FROM user WHERE id = ?";
        PreparedStatement checkUserStatement = conn.prepareStatement(checkUserQuery);
        checkUserStatement.setInt(1, userId);
        ResultSet checkUserResult = checkUserStatement.executeQuery();

        if (checkUserResult.next()) {
            System.out.println("用户信息");
            System.out.println("1. 用户名");
            System.out.println("2. 密码");
            System.out.println("3. 邮箱");
            System.out.println("4. 电话");
            System.out.println("5. 返回上级菜单");
            System.out.print("请输入要更新的信息编号：");
            int infoChoice = scanner.nextInt();

            if (infoChoice >= 1 && infoChoice <= 4) {
                scanner.nextLine(); // Consume the newline character

                System.out.print("请输入新的信息：");
                String newInfo = scanner.nextLine();

                // 执行更新用户信息的操作
                String updateInfoQuery = "";
                switch (infoChoice) {
                    case 1:
                        updateInfoQuery = "UPDATE user SET username = ? WHERE id = ?";
                        break;
                    case 2:
                        updateInfoQuery = "UPDATE user SET password = ? WHERE id = ?";
                        break;
                    case 3:
                        updateInfoQuery = "UPDATE user SET email = ? WHERE id = ?";
                        break;
                    case 4:
                        updateInfoQuery = "UPDATE user SET phone = ? WHERE id = ?";
                        break;
                }

                PreparedStatement updateInfoStatement = conn.prepareStatement(updateInfoQuery);
                updateInfoStatement.setString(1, newInfo);
                updateInfoStatement.setInt(2, userId);
                int rowsAffected = updateInfoStatement.executeUpdate();

                if (rowsAffected > 0) {
                    System.out.println("用户信息已更新");
                } else {
                    System.out.println("更新用户信息时出现错误");
                }
            } else if (infoChoice == 5) {
                System.out.println("正在返回上级菜单...");
            } else {
                System.out.println("无效的信息编号");
            }
        } else {
            System.out.println("无效的用户编号");
        }
    }

    private static void browseAndUpdateTicketInfo(Connection conn, Scanner scanner) throws SQLException {
        String query = "SELECT * FROM ticket";
        Statement statement = conn.createStatement();
        ResultSet resultSet = statement.executeQuery(query);

        System.out.println("车票信息");
        System.out.println("--------------------------------------------------");
        System.out.println("编号\t用户编号\t车辆编号\t购买时间");
        System.out.println("--------------------------------------------------");

        while (resultSet.next()) {
            int ticketId = resultSet.getInt("id");
            int userId = resultSet.getInt("user_id");
            int vehicleId = resultSet.getInt("vehicle_id");
            Timestamp purchaseTime = resultSet.getTimestamp("purchase_time");

            System.out.printf("%d\t%d\t\t%d\t\t%s%n", ticketId, userId, vehicleId, purchaseTime);
        }

        System.out.println("--------------------------------------------------");

        System.out.print("请输入要更新的车票编号：");
        int ticketId = scanner.nextInt();

        // 检查车票是否存在
        String checkTicketQuery = "SELECT * FROM ticket WHERE id = ?";
        PreparedStatement checkTicketStatement = conn.prepareStatement(checkTicketQuery);
        checkTicketStatement.setInt(1, ticketId);
        ResultSet checkTicketResult = checkTicketStatement.executeQuery();

        if (checkTicketResult.next()) {
            System.out.println("车票信息");
            System.out.println("1. 用户编号");
            System.out.println("2. 车辆编号");
            System.out.println("3. 购买时间");
            System.out.println("4. 返回上级菜单");
            System.out.print("请输入要更新的信息编号：");
            int infoChoice = scanner.nextInt();

            if (infoChoice >= 1 && infoChoice <= 3) {
                scanner.nextLine(); // Consume the newline character

                System.out.print("请输入新的信息：");
                String newInfo = scanner.nextLine();

                // 执行更新车票信息的操作
                String updateInfoQuery = "";
                switch (infoChoice) {
                    case 1:
                        updateInfoQuery = "UPDATE ticket SET user_id = ? WHERE id = ?";
                        break;
                    case 2:
                        updateInfoQuery = "UPDATE ticket SET vehicle_id = ? WHERE id = ?";
                        break;
                    case 3:
                        updateInfoQuery = "UPDATE ticket SET purchase_time = ? WHERE id = ?";
                        break;
                }

                PreparedStatement updateInfoStatement = conn.prepareStatement(updateInfoQuery);
                updateInfoStatement.setString(1, newInfo);
                updateInfoStatement.setInt(2, ticketId);
                int rowsAffected = updateInfoStatement.executeUpdate();

                if (rowsAffected > 0) {
                    System.out.println("车票信息已更新");
                } else {
                    System.out.println("更新车票信息时出现错误");
                }
            } else if (infoChoice == 4) {
                System.out.println("正在返回上级菜单...");
            } else {
                System.out.println("无效的信息编号");
            }
        } else {
            System.out.println("无效的车票编号");
        }
    }
}
