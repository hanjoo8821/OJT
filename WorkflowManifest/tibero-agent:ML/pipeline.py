import kfp
from kfp import dsl
from kubernetes.client.models import V1EnvVar

@dsl.pipeline(
    name = 'Tibero-ML-AB1_2',
    description = 'A Machine Learning pipeline with Tibero JDBC agent'
)

def ml_pipeline():
    v1 = dsl.VolumeOp(
        name = "pv1",
        resource_name = "pvc1",
        modes = dsl.VOLUME_MODE_RWM,
        size = "100Mi"
    )

    pod1 = dsl.ContainerOp(
        name = 'Tibero-JDBC agent',
        image = 'hanjoo8821/jdbc-tibero:colsout-0.2',
        container_kwargs={'env':[V1EnvVar('id', 'hanjoo'), V1EnvVar('pw', '1010'), V1EnvVar('tab', 'AB1_2'), V1EnvVar('id1', 'EMP_NUM'), V1EnvVar('id2', 'BIRTH'), V1EnvVar('id3', 'NAME')]},
        pvolumes = {"/Output": v1.volume}
    )

    pod2a = dsl.ContainerOp(
        name = 'Trans-EMP_NUM',
        image = 'hanjoo8821/jdbc-tibero:trans-emp-0.2',
        command = ['sh', '-c'],
        arguments = ['python trans-emp_num.py EMP_NUM'],
        pvolumes = {"/Output": pod1.pvolume}
    )

    pod2b = dsl.ContainerOp(
        name = 'Trans-BIRTH',
        image = 'hanjoo8821/jdbc-tibero:trans-birth-0.2',
        command = ['sh', '-c'],
        arguments = ['python trans-birth.py BIRTH'],
        pvolumes = {"/Output": pod1.pvolume}
    )

    pod2c = dsl.ContainerOp(
        name = 'Print',
        image = 'alpine:3.6',
        command = ['cat', '/Output/NAME.txt'],
        pvolumes = {"/Output": pod1.pvolume}
    )

    pod3a = dsl.ContainerOp(
        name = 'Print',
        image = 'alpine:3.6',
        command = ['cat', '/Output/EMP_NUM_trans.txt'],
        pvolumes = {"/Output": pod2a.pvolume}
    )

    pod3b = dsl.ContainerOp(
        name = 'Print',
        image = 'alpine:3.6',
        command = ['cat', '/Output/BIRTH_trans.txt'],
        pvolumes = {"/Output": pod2b.pvolume}
    )

if __name__ == '__main__':
    kfp.compiler.Compiler().compile(ml_pipeline, __file__ + '.tar.gz')