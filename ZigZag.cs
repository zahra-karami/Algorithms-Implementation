namespace Algorithms
{
    public class ZigZag
    {
        /*
        Convert array into Zig-Zag fashion
        Given an array of DISTINCT elements, rearrange the elements of array in zig-zag fashion in O(n) time. 
        The converted array should be in form a < b > c < d > e < f.
        Example:
        Input: arr[] = {4, 3, 7, 8, 6, 2, 1}
        Output: arr[] = {3, 7, 4, 8, 2, 6, 1}
        */

        private readonly int[] _arr;
        public ZigZag(int[] arr)
        {
            _arr = arr;
        }
        public int[] Do()
        {
            var n = _arr.Length - 1;
            var flag = true;
            var i = 0;

            while (i < n)
            {
                if (!flag && _arr[i] < _arr[i + 1])
                {
                    Swap(i);
                }
                else if (flag && _arr[i] > _arr[i + 1])
                {
                    Swap(i);
                }
                i++;
                flag = !flag;
            }

            return _arr;

        }

        private void Swap(int i)
        {
            var temp = _arr[i];
            _arr[i] = _arr[i + 1];
            _arr[i + 1] = temp;
        }
    }
}
