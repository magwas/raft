export MODEL_BASENAME=raft
export REPO_NAME=raft
export GITHUB_ORGANIZATION=magwas
export LANGUAGE=java
export JAVA_TARGET=none
export CONSISTENCY_INPUTS=raft.rich 

all: raft.compiled

include /usr/share/zenta-tools/model.rules

clean:
	git clean -fdx


