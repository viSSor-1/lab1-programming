
#include <iostream>
// Функция вычисления квадрата числа
auto square(int x) -> int {
return x * x;
}
int main() {
    
// Униформ-инициализация
auto number{7};
// Вызов функции
auto result = square(number);
std::cout << "Число: " << number << std::endl;
std::cout << "Квадрат: " << result << std::endl;
return 0;
}

