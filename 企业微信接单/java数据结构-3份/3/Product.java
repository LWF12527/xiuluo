class Product {
    private int productId; // 主关键字
    private String productName;
    private double price;
    private int stock;
    private String category;

    public Product(int productId, String productName, double price, int stock, String category) {
        this.productId = productId;
        this.productName = productName;
        this.price = price;
        this.stock = stock;
        this.category = category;
    }

    public int getProductId() {
        return productId;
    }

    public String getProductName() {
        return productName;
    }

    public double getPrice() {
        return price;
    }

    public int getStock() {
        return stock;
    }

    public String getCategory() {
        return category;
    }

    @Override
    public String toString() {
        return "Product{" +
                "productId=" + productId +
                ", productName='" + productName + '\'' +
                ", price=" + price +
                ", stock=" + stock +
                ", category='" + category + '\'' +
                '}';
    }
}
