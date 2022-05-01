class Foo {
    volatile int sequence;
    public Foo() {
        sequence = 0;
    }

    public void first(Runnable printFirst) throws InterruptedException {
        
        // printFirst.run() outputs "first". Do not change or remove this line.
        printFirst.run();
        sequence = 1;
    }

    public void second(Runnable printSecond) throws InterruptedException {
        
        // printSecond.run() outputs "second". Do not change or remove this line.
        while(sequence != 1){}
        printSecond.run();
        sequence = 2;
    }

    public void third(Runnable printThird) throws InterruptedException {
        
        // printThird.run() outputs "third". Do not change or remove this line.
        while(sequence != 2){}
        printThird.run();
        sequence = 3;
    }
}