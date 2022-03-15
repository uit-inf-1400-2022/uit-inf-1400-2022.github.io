
// Example of method overloading using Java
class Main {
    void f(int x) {
        System.out.println(x*x);
    }

    void f(String x) {
        System.out.println(x);
    }

    public static void main(String[] args) {
        Main m = new Main();
        m.f("Hei");
        m.f(5);
    }
}

