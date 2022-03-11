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
interface _StoreCollect {
    storeName: string;
    persistedState: boolean;
    state: any;
    setter?: any[];
}
declare const createStore: (app: any, stores: _StoreCollect[]) => any;
export default createStore;
