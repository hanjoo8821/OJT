import kfp
import kfp.components as comp
from kfp import dsl
from kubernetes.client.models import V1EnvVar, V1SecretKeySelector

@dsl.pipeline(
    name='tibero-agent-dummy',
    description='jin tibero agent test'
)

def tibero_agent_pipeline():
    pod1 = dsl.ContainerOp(
        name="pod1",
        image="jjh2613/tibero-agent:3.0",
        container_kwargs={'env':[V1EnvVar('agent_ip', '192.1.4.31'), V1EnvVar('agent_port', '8629'), V1EnvVar('agent_id', 'tibero'), V1EnvVar('agent_pw', 'tmax'), V1EnvVar('agent_sql', 'SELECT * FROM ALL_USERS')]}
    )

    pod2 = dsl.ContainerOp(
        name="pod2",
        image="jjh2613/tibero-agent:3.0",
        container_kwargs={'env':[V1EnvVar('agent_ip', '192.1.4.31'), V1EnvVar('agent_port', '8629'), V1EnvVar('agent_id', 'tibero'), V1EnvVar('agent_pw', 'tmax'), V1EnvVar('agent_sql', 'SELECT * FROM ALL_USERS')]}
    )

    pod3 = dsl.ContainerOp(
        name="pod3",
        image="jjh2613/tibero-agent:3.0",
        container_kwargs={'env':[V1EnvVar('agent_ip', '192.1.4.31'), V1EnvVar('agent_port', '8629'), V1EnvVar('agent_id', 'tibero'), V1EnvVar('agent_pw', 'tmax'), V1EnvVar('agent_sql', 'SELECT * FROM ALL_USERS')]}
    )

    pod2.after(pod1)
    pod3.after(pod2)
    
if __name__ == "__main__":
    import kfp.compiler as compiler
    compiler.Compiler().compile(tibero_agent_pipeline, __file__ + ".tar.gz")
