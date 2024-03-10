from .nodes.egbdfy import EGBDAPINode
from .nodes.egcchq import EGTXCCHQ
from .nodes.egcgysqy import EGSCQYQBQYNode
from .nodes.egcjpjnode import EGCJPJNode
from .nodes.egjfzz import EGJFZZSC
from .nodes.egjxfz import EGJXFZNODE
from .nodes.egryqh import EGRYQHNode
from .nodes.egszqh import EGXZQHNode
from .nodes.egtjtxsy import EGCPSYTJNode
from .nodes.egtscdscjnode import EGTSCDSCJLNode
from .nodes.egtscdsdgnode import EGTSCDSDGLNode
from .nodes.egtscdsfgnode import EGTSCDSFGLNode
from .nodes.egtscdsjtnode import EGTSCDSJTLNode
from .nodes.egtscdsqtnode import EGTSCDSQTLNode
from .nodes.egtscdsrwnode import EGTSCDSRWLNode
from .nodes.egtscdssjdiy import EGSJNode
from .nodes.egtscdswpnode import EGTSCDSWPLNode
from .nodes.egtscdszlnode import EGTSCDSZLLNode
from .nodes.egtscmb import EGTSCMBGLNode
from .nodes.egtxljbc import EGTXBCLJBCNode
from .nodes.egwbpj import EGWBRYPJ
from .nodes.egwbsjpj import EGWBSJPJ
from .nodes.egysbhd import EGSCQYBHDQYYNode
from .nodes.egysblld import EGYSQYBLLDNode
from .nodes.egysqyld import EGYSQYBBLLDNode
from .nodes.egyssxqy import EGSCQSXQYNode
from .nodes.egzzbsyh import EGZZBSYH
from .nodes.egzzcjnode import EGTXZZCJNode
from .nodes.egzzhsyh import EGZZHSYH
from .nodes.egzzhtkz import EGZZKZHTNODE
from .nodes.egzzkzyh import EGZZSSKZNODE
from .nodes.egzzmhnode import EGZZBYYHNode
from .nodes.egwzsytj import EGYSZTNode
from .nodes.egwbksh import EGWBKSH
from .nodes.egtxzdljjz import EGJZRYTX
from .nodes.egtxcglj import EGTXLJNode
from .nodes.egtxystz import EGHTYSTZNode
from .nodes.egtxwhlj import EGWHLJ
from .nodes.egzzcjpj import EGZZHBCJNode
from .nodes.EGJDFDHT import EGRYHT
from .nodes.EGSZJDYS import EGSZJDYS
from .nodes.EGSZHZ import EG_SS_RYZH
from .nodes.EGWBZYSRK import EGZYWBKNode
from .nodes.EGZZTXHZ import EGTXZZZHNode
from .nodes.EGJBCHBMQ import EGJBCH

NODE_CLASS_MAPPINGS = {
    "EG_FX_BDAPI": EGBDAPINode,
    "EG_TX_CCHQ": EGTXCCHQ,
    "EG_SCQY_QBQY": EGSCQYQBQYNode,
    "EG_TX_CJPJ": EGCJPJNode,
    "EG_JF_ZZSC": EGJFZZSC,
    "EG_JXFZ_node": EGJXFZNODE,
    "EG_WXZ_QH": EGRYQHNode,
    "EG_XZ_QH": EGXZQHNode,
    "EG_CPSYTJ": EGCPSYTJNode,
    "EG_TSCDS_CJ": EGTSCDSCJLNode,
    "EG_TSCDS_DG": EGTSCDSDGLNode,
    "EG_TSCDS_FG": EGTSCDSFGLNode,
    "EG_TSCDS_JT": EGTSCDSJTLNode,
    "EG_TSCDS_QT": EGTSCDSQTLNode,
    "EG_TSCDS_RW": EGTSCDSRWLNode,
    "EG_SJ" : EGSJNode,
    "EG_TSCDS_WP": EGTSCDSWPLNode,
    "EG_TSCDS_ZL": EGTSCDSZLLNode,
    "EG_TSCMB_GL": EGTSCMBGLNode,
    "EG_TX_LJBC": EGTXBCLJBCNode,
    "EG_TC_Node": EGWBRYPJ,
    "EG_SJPJ_Node" : EGWBSJPJ,
    "EG_SCQY_BHDQY": EGSCQYBHDQYYNode,
    "EG_YSQY_BLLD": EGYSQYBLLDNode,
    "EG_YSQY_BBLLD": EGYSQYBBLLDNode,
    "EG_SCQY_SXQY": EGSCQSXQYNode,
    "EG_ZZ_BSYH": EGZZBSYH,
    "ER_TX_ZZCJ": EGTXZZCJNode,
    "EG_ZZ_HSYH": EGZZHSYH,
    "EG_ZZKZ_HT_node": EGZZKZHTNODE,
    "EG_ZZ_SSKZ": EGZZSSKZNODE,
    "EG_ZZ_BYYH": EGZZBYYHNode,
    "EG-YSZT-ZT" : EGYSZTNode,
    "EG_WB_KSH": EGWBKSH,
    "EG_TX_JZRY" : EGJZRYTX,
    "EG_TX_LJ" : EGTXLJNode,
    "EG_HT_YSTZ" : EGHTYSTZNode,
    "EG_TX_WHLJ" : EGWHLJ,
    "EG_ZZHBCJ" : EGZZHBCJNode,
    "EG_RY_HT" : EGRYHT,
    "EG_SZ_JDYS" : EGSZJDYS,
    "EG_SS_RYZH" : EG_SS_RYZH,
    "EG_ZY_WBK" : EGZYWBKNode,
    "EG_TXZZ_ZH" : EGTXZZZHNode,
    "ER_JBCH": EGJBCH,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "EG_FX_BDAPI" : "2🐕Baidu Translation API",
    "EG_TX_CCHQ" : "2🐕Image size acquisition",
    "EG_SCQY_QBQY" : "2🐕Regular color migration",
    "EG_TX_CJPJ" : "2🐕Image cropping data stitching",
    "EG_JF_ZZSC" : "2🐕Seam Mask Generator",
    "EG_JXFZ_node" : "2🐕Image Mirror Flip",
    "EG_WXZ_QH" : "2🐕Unrestricted switching",
    "EG_XZ_QH" : "2🐕Choice Switch",
    "EG_CPSYTJ" : "2🐕Add finished watermark image",
    "EG_TSCDS_CJ" : "2🐕Scene class",
    "EG_TSCDS_DG" : "2🐕Lighting Class",
    "EG_TSCDS_FG" : "2🐕Style category",
    "EG_TSCDS_JT" : "2🐕Lens class",
    "EG_TSCDS_QT" : "2🐕Other categories",
    "EG_TSCDS_RW" : "2🐕Character category",
    "EG_SJ" : "2🐕Random prompt",
    "EG_TSCDS_WP" : "2🐕Item category",
    "EG_TSCDS_ZL" : "2🐕Quality category",
    "EG_TSCMB_GL" : "2🐕Custom template",
    "EG_TX_LJBC" : "2🐕Specify image save path",
    "EG_TC_Node" : "2🐕Text arbitrary splicing",
    "EG_SJPJ_Node" : "2🐕Text random splicing",
    "EG_SCQY_BHDQY" : "2🐕Saturation migration",
    "EG_YSQY_BLLD" : "2🐕Preserve brightness",
    "EG_YSQY_BBLLD" : "2🐕Do not retain brightness",
    "EG_SCQY_SXQY" : "2🐕Hue migration",
    "EG_ZZ_BSYH" : "2🐕Mask Blurred white edges",
    "ER_TX_ZZCJ" : "2🐕Cropping image mask areas",
    "EG_ZZ_HSYH" : "2🐕Mask Blurred Black edges",
    "EG_ZZKZ_HT_node" : "2🐕Mask slider extension",
    "EG_ZZ_SSKZ" : "2🐕Mask Expansion",
    "EG_ZZ_BYYH" : "2🐕Mask edges blurred",
    "EG-YSZT-ZT" : "2🐕Text watermark addition",
    "EG_WB_KSH": "2🐕View Text",
    "EG_TX_JZRY" : "2🐕Load any image",
    "EG_TX_LJ" : "2🐕Conventional filters",
    "EG_HT_YSTZ" : "2🐕Color adjustment",
    "EG_TX_WHLJ" : "2🐕Internet celebrity filter",
    "EG_ZZHBCJ" : "2🐕Mask can be cut arbitrarily",
    "EG_RY_HT" : "2🐕Simple slider",
    "EG_SZ_JDYS" : "2🐕+-x÷",
    "EG_SS_RYZH" : "2🐕Int Float Text Swap",
    "EG_ZY_WBK" : "2🐕Free input box",
    "EG_TXZZ_ZH" : "2🐕Mask image exchange",
    "ER_JBCH": "2🐕Redraw encoder",
}
