import kfp
import kfp.components as comp
from kfp import dsl
from kubernetes.client.models import V1EnvVar, V1SecretKeySelector

@dsl.pipeline(
    name = "tibero-agent-test",
    description = "Hanjoo's tibero agent : test version"
)

def tibero_agent_pipeline():
    pod1 = dsl.ContainerOp(
        name = "pod1",
        image = "sqlagent:0.1",
        container_kwargs = {'env':[V1EnvVar('id', 'hanjoo'), V1EnvVar('pw', '1010')]}
    )

    pod2a = dsl.ContainerOp(
        name = "pod2a",
        image = "sqlagent:0.2"
    )

    pod2b = dsl.ContainerOp(
        name = "pod2b",
        image = "sqlagent:0.2"
    )

    pod3 = dsl.ContainerOp(
        name = "pod3",
        image = "sqlagent:0.1",
        container_kwargs = {'env':[V1EnvVar('id', 'hanjoo'), V1EnvVar('pw', '1010')]}
    )

    pod2a.after(pod1)
    pod2b.after(pod1)
    pod3.after(pod2a, pod2b)
    
if __name__ == "__main__":
    import kfp.compiler as compiler
    compiler.Compiler().compile(tibero_pipeline_test, __file__ + ".tar.gz")
