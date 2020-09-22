import kfp
from kfp import dsl
from kubernetes.client.models import V1EnvVar

def vol_op(n):
    return dsl.VolumeOp(
        name = n,
        resource_name = "pvc",
        modes = dsl.VOLUME_MODE_RWM,
        size = "100Mi"
    )

def query_op_vol(n, vol):
    return dsl.ContainerOp(
        name = n,
        image = "hanjoo8821/jdbc-tibero:null",
        container_kwargs = {'env': [V1EnvVar('id', 'hanjoo'), V1EnvVar('pw', '1010')]},
        command = ['sh', '-c'],
        arguments = ['java -cp "./JdbcAgentEx-null.jar:./tibero6jdbc-1.0.jar" local.hanjoo.JdbcAgent "$id" "$pw" | tee /data/output'],
        pvolumes = {"/data": vol}
    )

def print_op_vol(n, vol):
    return dsl.ContainerOp(
        name = n,
        image = "hanjoo8821/jdbc-tibero:null",
        command = ['cat', '/data/output'],
        pvolumes = {"/data": vol}
    )

@dsl.pipeline(
    name = "tibero-agent:vol",
    description = "Hanjoo's tibero agent : vol version"
)

def tibero_pipeline_vol():

    vop1 = vol_op("Test-PV")
    sql1 = query_op_vol("SQL", vop1.volume)
    print1 = print_op_vol("Print", sql1.pvolume)
    
if __name__ == "__main__":
    kfp.compiler.Compiler().compile(tibero_pipeline_vol, __file__ + ".tar.gz")