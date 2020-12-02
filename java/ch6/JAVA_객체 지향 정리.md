[toc]



# JAVA_객체 지향 정리

### 클래스와 객체

1. 클래스 (class)
   - 정의 : 객체를 정의해 놓은것
   - 용도 : 객체를 생성하는데 사용
2. 객체
   - 정의 : 실제로 존재하는 것, 사물 또는 개념
   - 용도 : 객체가 가지고 있는 기능과 속성에 따라 다름

| 클래스      | 객체   |
| ----------- | ------ |
| 제품 설계도 | 제품   |
| TV 설계도   | TV     |
| 붕어빵 기계 | 붕어빵 |

객체를 만드는 과정을 `인스턴스화`라고 한다.

클래스로 부터 만들어진 객체를 `인스턴스`



책상은 인스턴스다 -> 책상은 `객체`다

책상은 책상클래스의 객체다 -> 책상은 책상클래스의 `인스턴스`다

- 의미는 같지만 문맥상 다르게 쓰기.

### 객체의 구성요소

1. 속성
   - 멤버변수, 특성, 필드, 상태
2. 기능
   - 메서드, 함수, 행위

- 객체는 속성과 기능의 집합
- 속성과 기능은 객체의 멤버.

 

### 인스턴스와 참조 변수

인스턴스와 참조 변수는 TV와 TV리모콘과 같은 관계이다. : 참조변수를 통해 인스턴스를 다루기때문

```java
Tv t; //참조변수 t선언
t= new Tv(); // 인스턴스 생성
```

- 인스턴스는 참조변수를 통해서만 다룰 수 있으며, 참조변수의 타입은 인스턴스의 타입과 일치 해야 한다. 



### java 예제 정리

```java
class Tv {
    // Tv의 속성( 멤버 변수 )
    String color;
    boolean power;
    int channel;
    // Tv의 기능(메서드)
    void power() {power = !power;}
    void channelUp() {
        ++channel;
    }
    void channelDown() {
        --channel;
    }
}
```

```java
public class TvTest3 {
    public static void main(String[] args){
        Tv t1 = new Tv();
        Tv t2 = new Tv();
        t2 = t1; // t1이 저장하고 있는 값(주소)을 t2에 저장.
        //t2가 참조하던 인스턴스는 더 이상 사용할 수 없음.
        //t1의 인스턴스를 참조하게 된다.
        t1.channel = 8;
		// t1.channel, t2.channel == 8
        // 하나의 인스턴스를 여러개의 참조변수가 참조할 수 있다
        // 하나의 참조변수는 여러개의 인스턴스를 참조할 수 없다.

    }
}
```



### 객체 배열

```java
public class TvTest4 {
    public static void main(String[] args){
        // 배열은 조금 다르다.
        //1
        Tv[] tvArr = new Tv[3]; // 길이가 3인 Tv 타입의 참조배열 변수
        for (int i=0; i<tvArr.length;i++) {
            tvArr[i] = new Tv(); // 객체를 생성해서 각 배열에 저장.
            // 추가적인 내용은 다형성 배울때 알게 됨.
            tvArr[i].channel = i + 10;
        }
        //2
        /*
        Tv[] tvArr = new Tv[3];
        tvArr[1] = new Tv();
        tvArr[2] = new Tv();
        tvArr[3] = new Tv();
        */
        //3
        // Tv[] tvArr = {new Tv(), new Tv(), new Tv()};
        for (int i = 0; i<tvArr.length;i++){
            tvArr[i].channelUp();
            System.out.printf("%d : %d%n", i, tvArr[i].channel);

        }
    }
}

```

