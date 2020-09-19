import kfp
from kfp import dsl

@dsl.pipeline(
    name = "tibero-agent-test",
    description = "Hanjoo's tibero agent : test version"
)

def tibero_pipeline_test():
    pod1 = dsl.ContainerOp(
        name = "pod1",
        image = "hanjoo8821/tibero-agent:basic"
    )

    pod2a = dsl.ContainerOp(
        name = "pod2a",
        image = "hanjoo8821/tibero-agent:basic"
    )

    pod2b = dsl.ContainerOp(
        name = "pod2b",
        image = "hanjoo8821/tibero-agent:basic"
    )

    pod3 = dsl.ContainerOp(
        name = "pod3",
        image = "hanjoo8821/tibero-agent:basic"
    )

    pod2a.after(pod1)
    pod2b.after(pod1)
    pod3.after(pod2a, pod2b)
    
if __name__ == "__main__":
    kfp.compiler.Compiler().compile(tibero_pipeline_test, __file__ + ".tar.gz")