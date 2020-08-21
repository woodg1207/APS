import java.util.function.Function;

public class HelloWorld {
    public static void main(String[] args) {
		int x=10;
		int y=20;
		System.out.println("x = "+x);
		System.out.println("y = "+y);
		// System.out.printf(a.test(1));
		switch (x) {
			case 10 :
				System.out.println("hello");
				break;
			case 2:
				System.out.println("world");
		}
		int[] arr = new int[5];
		System.out.println(arr);
		for (int i=0; i<arr.length; i++){
			System.out.println(arr[i]);
			arr[i] = i;
			System.out.println(arr[i]);
		}
		System.out.println(arr.length);
	}
}
