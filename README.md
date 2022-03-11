#### Hellow! ####

* 在ts+vue3.0的环境下基于provide和inject函数的小小插件，代码只有二十行，后面会根据我自己的需求进行封装 
    > 这是我自用的全局状态小插件，目前只是做了简单的全局状态存储以及同步函数setter，后面有时间或者有需求再加上异步处理状态，内部接口等等

![我是图片](https://img1.baidu.com/it/u=2753860582,1141882953&fm=26&fmt=auto&gp=0.jpg)
* * *

* 实现
  + 利用proxy处理响应数据
  + 利用session做持久化并监听数据更新session
  + 将所有setter解构放到store对象上
  + 返回store

 使用直接贴代码
 ============

 > npm i xins.store.plugin


新建store文件夹 store/index.ts代码如下，记得createApp之后use一下
```
import { App } from "vue";
import createStore from 'xins.store.plugin'
import TestModule from './module_Test'
export default (app:App) => {
    createStore(app,[TestModule])
}
```

store文件夹下新建module_Test文件夹  module_Test/index.ts代码如下
```
import setter from './setter'
import state from './state'
export default {
    storeName: 'test',
    persistedState: false,
    state,
    setter
}
```

module_Test/setter.ts代码如下
``` 
export const acticleA = {
    'setUser': function (payload:any) {
        this.user = payload
    },
    'removeUser': function () {
        this.user = null
    }
}
export default [acticleA]
```

module_Test/state.ts代码如下
``` 
export default {
    user: {
        name: '张三'
    }
}
```

在项目页面使用
``` 
// 获取test模块的所有state及setter函数
const storeStateTest = inject('test')
const { proxy } = getCurrentInstance()
console.log(proxy.$Store['test'],'test的setter')
console.log(storeStateTest,'test的state')
```


完结 

email：~~kaburda@163.com~~
