import { watch, readonly, reactive } from "vue";
/**
 * 此脚本暴露三个方法 
 * ***************
 * @createStore //// 用于创建仓库列表
 * @params //// 每个仓库包含自己的 state(reactive) setter 方法，获取state使用inject('仓库名称')
 * [
 *  {
 *      storeName:string  // 仓库名称
 *      persistedState: boolean // 是否开启持久化储存，依赖于sessionStorage
 *      state: {
 *      }
 *      setter: [
 *          {
 *              'setter-item-name': fn // fn不能使用箭头函数的形式
 *          }
 *      ]
 *  }
 * ]
 * setter中的fn接收传递过来的数据，可以通过this.***得到当前仓库的state内的数据进行修改
 *  */
// interface _StoreCollect {
//     storeName: string
//     persistedState: boolean
//     state: any
//     setter?: any[]
// }
const createStore = (app:any, stores) => {
    if(!stores?.length) {return} 
    let AllStore:any = []
    stores.map(ele => {
        // 包装成响应式 
        // ele.state = reactive(ele.state)
        // 注入
        app.provide(ele.storeName, readonly(ele.state)) // 这里标记，后面可以优化
        // 持久化处理
        if (ele.persistedState) {
            // 读取sessionStorage的值
            const storageState = JSON.parse(sessionStorage.getItem(ele.storeName) || "{}");
            for (const key in storageState) {
                ele.state[key] = storageState[key];
            }
            // 监听值变化，保存到sessionStorage
            watch(
                () => ele.state,
                () => {
                    sessionStorage.setItem(ele.storeName, JSON.stringify(ele.state));
                },
                { deep: true }
            );
        }
        // 扁平化setter
        AllStore[ele.storeName] = {}
        ele.setter && ele.setter.map(setterItem => {
            for(var fnName in setterItem) {
                AllStore[ele.storeName][fnName] = setterItem[fnName].bind(ele.state)
            }
        });
        // 不需要暴露state可以更好的控制单向流
        // AllStore[ele.storeName]['state'] = ele.state
        // 不处理state数据类型，需要你自己去写范型哦
    })
    // 注册全局对象，需要在模块文件写下面代码最好在入口文件里面写，ts的编译问题
    /**
     *  declare module '@vue/runtime-core' {
     *      interface ComponentCustomProperties {
     *          $Store: any 
     *      }
     *  }
     */
    app.config.globalProperties.$Store = AllStore;
    return AllStore
}

export default createStore;





