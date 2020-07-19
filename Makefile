export MODEL_BASENAME=raft
export REPO_NAME=raft
export GITHUB_ORGANIZATION=magwas
export LANGUAGE=java
export JAVA_TARGET=none
export CONSISTENCY_INPUTS=raft.rich 
export TOOLCHAINDIR=/usr/local/toolchain

all: target/zentaworkaround.ok raft.compiled Tile_with_walls.png

include /usr/share/zenta-tools/model.rules

dia:
	sudo apt -y install dia

Tile_with_walls.png: dia
	dia Tile_with_walls.dxf -e Tile_with_walls.png
clean:
	rm -rf raft
	git clean -fdx

target/zentaworkaround.ok: 
	mkdir -p target
	mkdir -p ~/.zenta/.metadata/.plugins/org.eclipse.e4.workbench/
	cp $(TOOLCHAINDIR)/etc/workbench.xmi ~/.zenta/.metadata/.plugins/org.eclipse.e4.workbench/
	touch target/zentaworkaround.ok

