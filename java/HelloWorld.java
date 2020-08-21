import java.util.function.Function;

public class HelloWorld {
    public static void main(String[] args) {
		int x=10;
		int y=20;
		Hello a = new Hello();
		System.out.println("x="+x);
		System.out.println("y="+y);
		// System.out.println();
		switch (x) {
			case 10 :
				System.out.println("hello");
				break;
			case 2:
				System.out.println("world");
		}

	}
}

class Hello {
	public static void main(String[] args) {
		System.out.println("'hello'");
	}
	
}