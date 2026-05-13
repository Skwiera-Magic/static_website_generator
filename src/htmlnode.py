class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise Exception(NotImplementedError)

    def props_to_html(self):
        if self.props == None:
            return ""
        props = ""
        for prop in self.props:
            props += f' {prop}="{self.props[prop]}"'
        return props

    def __repr__(self):
        node = HTMLNode
        print(node)