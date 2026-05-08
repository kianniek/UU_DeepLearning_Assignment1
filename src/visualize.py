import sys
from pathlib import Path

THIS_DIR = Path(__file__).resolve().parent
PLOTNN_DIR = THIS_DIR.parent / "PlotNeuralNet"
sys.path.append(str(PLOTNN_DIR))
from pycore.tikzeng import *

# defined your arch
arch = [
    to_head('../PlotNeuralNet'),
    to_cor(),
    to_begin(),
    to_Conv("input", "T", 1, offset="(0,0,0)", to="(0,0,0)", height=18, depth=18, width=1, caption="Input"),
    to_Conv("perm1", "T", 1, offset="(1.5,0,0)", to="(input-east)", height=14, depth=14, width=1, caption="Perm1"),
    to_connection("input", "perm1"),
    to_ConvConvRelu("convrelu", "T", (16,16), offset="(1.5,0,0)", to="(perm1-east)", height=20, depth=20, width=(2,2), caption="Conv1D ReLU"),
    to_connection("perm1", "convrelu"),
    to_Conv("perm2", "T", 16, offset="(2,0,0)", to="(convrelu-east)", height=16, depth=16, width=1.5, caption="Perm2"),
    to_connection("convrelu", "perm2"),
    to_Conv("lstm", "T", 64, offset="(2,0,0)", to="(perm2-east)", height=24, depth=24, width=2.5, caption="LSTMx2"),
    to_connection("perm2", "lstm"),
    to_Conv("last", 1, 64, offset="(1.8,0,0)", to="(lstm-east)", height=8, depth=8, width=1.2, caption="Last t"),
    to_connection("lstm", "last"),
    to_Conv("fc", 1, 1, offset="(1.5,0,0)", to="(last-east)", height=6, depth=6, width=1.2, caption="FC"),
    to_connection("last", "fc"),
    to_Conv("output", 1, 1, offset="(1.5,0,0)", to="(fc-east)", height=4, depth=4, width=1, caption="Output"),
    to_connection("fc", "output"),
    r"""
\node[draw, rounded corners, align=left, anchor=north west, font=\small, fill=white, opacity=0.95, text opacity=1]
at ([xshift=0.8cm,yshift=2.0cm]output-east) {
CNN-LSTM model legend\\
Input: (B,T,1)\\
Perm1: (B,1,T)\\
Conv1D ReLU: channels 1 to 16, k=3, p=1\\
Perm2: (B,T,16)\\
LSTMx2: hidden=64, output (B,T,64)\\
Last t: out[:, -1, :] to (B,64)\\
FC: Linear 64 to 1\\
Output: (B,1)
};
""",
    to_end()
    ]

def main():
    namefile = Path(sys.argv[0]).stem
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()