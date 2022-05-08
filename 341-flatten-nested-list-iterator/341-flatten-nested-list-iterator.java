/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * public interface NestedInteger {
 *
 *     // @return true if this NestedInteger holds a single integer, rather than a nested list.
 *     public boolean isInteger();
 *
 *     // @return the single integer that this NestedInteger holds, if it holds a single integer
 *     // Return null if this NestedInteger holds a nested list
 *     public Integer getInteger();
 *
 *     // @return the nested list that this NestedInteger holds, if it holds a nested list
 *     // Return empty list if this NestedInteger holds a single integer
 *     public List<NestedInteger> getList();
 * }
 */
public class NestedIterator implements Iterator<Integer> {
    List<Integer> arr;
    int index;
    public NestedIterator(List<NestedInteger> nestedList) {
        arr = new ArrayList<>();
        for(NestedInteger item : nestedList) {
            build(item);
        }
        index = 0;
    }
    
    public void build(NestedInteger item) {
        if(item.isInteger()) arr.add(item.getInteger());
        else {
            for(NestedInteger element : item.getList()) {
                build(element);
            }
        }
    }

    @Override
    public Integer next() {
        return arr.get(index++);
    }

    @Override
    public boolean hasNext() {
        return index < arr.size();
    }
}

/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i = new NestedIterator(nestedList);
 * while (i.hasNext()) v[f()] = i.next();
 */