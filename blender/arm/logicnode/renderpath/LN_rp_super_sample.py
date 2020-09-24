from arm.logicnode.arm_nodes import *

class RpSuperSampleNode(ArmLogicTreeNode):
    """Use to set the supersampling quality."""
    bl_idname = 'LNRpSuperSampleNode'
    bl_label = 'Rp Super-sampling'
    arm_version = 1
    property0: EnumProperty(
        items = [('1', '1', '1'),
                 ('1.5', '1.5', '1.5'),
                 ('2', '2', '2'),
                 ('4', '4', '4')
                 ],
        name='', default='1')

    def init(self, context):
        super(RpSuperSampleNode, self).init(context)
        self.add_input('ArmNodeSocketAction', 'In')
        self.add_output('ArmNodeSocketAction', 'Out')

    def draw_buttons(self, context, layout):
        layout.prop(self, 'property0')

add_node(RpSuperSampleNode, category=PKG_AS_CATEGORY)