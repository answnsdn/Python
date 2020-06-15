#클래스 객체 생성(클래스 정의)
class Person:
    name = '꽃 -  김춘수'
    content = '내가 그의 이름을 불러주기 전에는 그는 다만 하나의 몸짓에 지나지 않았다.'

    def greeting(self):
        return f'{self,name}을 소개합니다.'

    def reading(self):
        return f'{self,name}의 내용은 {self,content}로 시작합니다.'

    @classmethod
    def person_means(cls):
        return f'{cls,name}은 김춘수의 명작이다.'

p1 = Person()
print(p1.person_means())