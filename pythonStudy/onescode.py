# coding = utf-8

class getDialogue(object):
    def continued(self,text):
        text = text.replace("吗", "")
        text = text.replace("?", "!")
        text = text.replace("？", "!")r
        return text

if __name__ == '__main__':
    print("你要说点什么？")
    while True:
        dialogue = input("\n我:")
        _class = getDialogue()
        if dialogue == '再见':
            exit('再见！')
        else:
            feedback = _class.continued(dialogue)
            print(feedback)