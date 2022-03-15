
// Abstract class with interface in Java

interface SubscriberInterface {
    void receive(String message);
}

abstract class Subscriber implements SubscriberInterface {
    
    String name;

    Subscriber(String name) {
        this.name = name;
    }

    public abstract void receive(String message);
}

class EmailSubscriber extends Subscriber {

    EmailSubscriber(String name) {
        super(name);
    }

    public void receive(String message) {
        System.out.println(this.name + " received e-mail " + message);
    }
}

class SubMain {
    public static void main(String[] args) {
        EmailSubscriber s = new EmailSubscriber("Arne");
        s.receive("Tilbud");
    }
}