from concretefactory1 import ConcreteFactory1
from concretefactory2 import ConcreteFactory2


def main(factory):    
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(f"{product_b.useful_function_b()}")
    print(f"{product_b.another_useful_function_b(product_a)}", end="")


if __name__ == "__main__":
    """
    The client code can work with any concrete factory class.
    """
    print("Client: Testing client code with the first factory type:")
    main(ConcreteFactory1())

    print("\n")

    print("Client: Testing the same client code with the second factory type:")
    main(ConcreteFactory2())