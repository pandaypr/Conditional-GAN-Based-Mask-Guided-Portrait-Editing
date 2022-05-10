
import sys
sys.path.append('../')
from pycore.tikzeng import *
from pycore.blocks  import *

arch = [ 
    to_head('..'), 
    to_cor(),
    to_begin(),
    
    #input
    to_input( '../examples/fcn8s/pic sample.png' ),

    #block-001
    to_ConvConvRelu( name='ccr_b1', s_filer=64, n_filer=(128,128), offset="(0,0,0)", to="(0,0,0)", width=(2,2), height=40, depth=40  ),
    to_Pool(name="pool_b1", offset="(0,0,0)", to="(ccr_b1-east)", width=1, height=32, depth=32, opacity=0.5),
    
    *block_2ConvPool( name='b2', botton='pool_b1', top='pool_b2', s_filer=256, n_filer=128, offset="(1,0,0)", size=(32,32,3.5), opacity=0.5 ),
    *block_2ConvPool( name='b3', botton='pool_b2', top='pool_b3', s_filer=128, n_filer=256, offset="(1,0,0)", size=(25,25,4.5), opacity=0.5 ),
    *block_2ConvPool( name='b4', botton='pool_b3', top='pool_b4', s_filer=64,  n_filer=512, offset="(1,0,0)", size=(16,16,5.5), opacity=0.5 ),
    *block_2ConvPool( name='b5', botton='pool_b4', top='pool_b5', s_filer=32,  n_filer=512, offset="(1,0,0)", size=(8,8,5.5), opacity=0.5 ),
    *block_2ConvPool( name='b6', botton='pool_b5', top='pool_b6', s_filer=16,  n_filer=512, offset="(1,0,0)", size=(6,6,5.5), opacity=0.5 ),

    #Bottleneck
    #block-005
    to_ConvConvRelu( name='ccr_b7', s_filer=8, n_filer=(512,512), offset="(2,0,0)", to="(pool_b6-east)", width=(4,4), height=4, depth=4, caption="Bottleneck"),
    to_connection( "pool_b6", "ccr_b7"),

    #Decoder
    *block_Unconv( name="b8", botton="ccr_b7", top='end_b8', s_filer=16,  n_filer=512, offset="(2.1,0,0)", size=(6,6,5.0), opacity=0.5 ),
    to_skip( of='ccr_b6', to='ccr_res_b8'),
    *block_Unconv( name="b9", botton="ccr_b8", top='end_b9', s_filer=32,  n_filer=512, offset="(2.1,0,0)", size=(8,8,5.0), opacity=0.5 ),
    to_skip( of='ccr_b5', to='ccr_res_b9'),
    *block_Unconv( name="b10", botton="ccr_b9", top='end_b10', s_filer=64,  n_filer=512, offset="(2.1,0,0)", size=(16,16,5.0), opacity=0.5 ),
    to_skip( of='ccr_b4', to='ccr_res_b10'),
    *block_Unconv( name="b11", botton="end_b10", top='end_b11', s_filer=128, n_filer=256, offset="(2.1,0,0)", size=(25,25,4.5), opacity=0.5 ),
    to_skip( of='ccr_b3', to='ccr_res_b11'),    
    *block_Unconv( name="b12", botton="end_b11", top='end_b12', s_filer=256, n_filer=128, offset="(2.1,0,0)", size=(32,32,3.5), opacity=0.5 ),
    to_skip( of='ccr_b2', to='ccr_res_b12'),    
    
    *block_Unconv( name="b13", botton="end_b12", top='end_b13', s_filer=512, n_filer=64,  offset="(2.1,0,0)", size=(40,40,2.5), opacity=0.5 ),
    to_skip( of='ccr_b1', to='ccr_res_b13'),
    
    to_ConvSoftMax( name="soft1", s_filer=512, offset="(0.75,0,0)", to="(end_b13-east)", width=1, height=40, depth=40, caption="RelU" ),
    to_connection( "end_b13", "soft1"),
    
    to_output( '../examples/fcn8s/mask.png', to='end_b13', xshift=2.5),
     
    to_end() 
    ]


def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()
    
