import kfp
from kfp import dsl

@dsl.pipeline(
    name = "hell_tmax",
    description = "Test - hell Tmax"
)

def hell_tmax(): 
    pod1 = dsl.ContainerOp(
        name = "pod1",
        image = "hanjoo8821/helltmax:0.1"
    )

    pod2a = dsl.ContainerOp(
        name = "pod2a",
        image = "hanjoo8821/helltmax:0.1"
    )

    pod2b = dsl.ContainerOp(
        name = "pod2b",
        image = "hanjoo8821/helltmax:0.1"
    )

    pod3 = dsl.ContainerOp(
        name = "pod3",
        image = "hanjoo8821/helltmax:0.1"
    )
    
    pod2a.after(pod1)
    pod2b.after(pod1)
    pod3.after(pod2a, pod2b)
    
if __name__ == "__main__":
    kfp.compiler.Compiler().compile(hell_tmax, __file__ + ".tar.gz")