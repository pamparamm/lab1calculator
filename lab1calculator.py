import os
from decimal import Decimal
from typing import Type

from methods.basemethod import IMethod
from methods.specialmethodpack import GaussMethod
from variants.v2 import V2


def main():
    variant = V2

    methods: list[Type[IMethod]] = IMethod.__subclasses__()
    steps = [Decimal("0.1"), Decimal("0.05"), Decimal("0.025")]

    output: list[str] = []

    output.append(f"🤡VARIANT🤡 {variant.__name__}")
    output.append(f"{'Etalon:':<10}{variant.etalon()}")
    output.append(f"{'Gauss 1:':<10}{GaussMethod.calc_gauss1(variant)}")
    output.append(f"{'Gauss 2:':<10}{GaussMethod.calc_gauss2(variant)}")
    output.append(f"{'Gauss 4:':<10}{GaussMethod.calc_gauss4(variant)}")

    margin = 2

    for method in methods:
        output.append(f"{'':<{margin}}🌟{method.__name__}")
        for step in steps:
            method_res = method.calc_quadrature(variant, step)
            runge_res = method.cptn_wrungel(variant, step)

            output.append(f"{'':<{2*margin}}{'Step:':<10}{step}")
            output.append(
                f"{'':<{2*margin}}{'N:':<10}{int((variant.b() - variant.a()) / step)}"
            )
            output.append(f"{'':<{2*margin}}{'Result:':<10}{method_res}")
            output.append(f"{'':<{2*margin}}{'Runge:':<10}{runge_res}")
            output.append(
                f"{'':<{2*margin}}{'Delta:':<10}{abs(variant.etalon() - method_res)}"
            )
            output.append(f"{'':<{2*margin}}{'P:':<10}{method.p()}")
            output.append(
                f"{'':<{2*margin}}{'P Fact:':<10}{method.p_fact(variant, step)}"
            )
            output.append(f"{'':<{2*margin}}{'---':<8}")

    filename = f"output/{variant.__name__}.yaml"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w", encoding="utf8") as Йамль:
        result = "\n".join(output)
        Йамль.write(result)
        print(result)


if __name__ == "__main__":
    main()
