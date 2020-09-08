from django.shortcuts import render

# Create your views here.
def home(request):
    Q_list = []
    A_list = []
    Q_list.append("Override / Overload의 차이점.")
    A_list.append("오버로딩 : 같은 이름의 메소드를 여러 개 가지면서 매개 변수를 다르게 정의하는 것 "+"\n"+" 오버라이딩 : 상위 클래스(부모 클래스)가 갖고 있는 메소드(자식 클래스)를 하위 클래스에서 재정의해 사용하는 것")
    ''''
    Q_list.append("Struct와 Class의 차이점.")
    Q_list.append("프로세스 생성 과정에 대해서 설명해보세요")
    Q_list.append("프로세스와 쓰레드의 차이를 설명해보세요")
    Q_list.append("Heap과 Stack의 차이점은 무엇인가요?")
    Q_list.append("TCP와 UDP의 차이점은?")
    Q_list.append("브라우저에서 주소창에 url 입력시 어떤일이 일어나는가?")
    Q_list.append("postgresql과 elastic search의 차이점은 무엇인가요?")
    Q_list.append("Quick sort에 대해서 설명해 줄 수 있나요?")
    Q_list.append("크롬 탭이 프로세스인지 쓰레드인지 설명해보세요")
    Q_list.append("Java Array와 ArrayList의 다른점.")
    Q_list.append("MVC 구조란?")
    Q_list.append("Override / Overload의 차이점.")
    Q_list.append("Override / Overload의 차이점.")
    '''
    return render(request, 'main.html', {'Q_list':Q_list, 'A_list':A_list})