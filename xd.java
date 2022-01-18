package com.company;
import com.sun.source.tree.Tree;

import java.util.*;
import java.util.Map.Entry;
public class xd {

    public static void main(String[] args) {
        HashMap<Integer, String> studenci = new HashMap<Integer, String>();
        studenci.put(1, "kowal");
        studenci.put(3, "kwowal");
        studenci.put(2, "kowdal");
        System.out.println(studenci);
        PriorityQueue<List> zadania = new PriorityQueue<List>(10, new ListComparator());
        //priorityqueue mozna uzyc po prostu zadania.add("kowalski") ale bez komparatora wtedy jest i zwykla kolejka wtedy
        List l1 = new List("cos",2);
        List l2 = new List("platki",1);
        zadania.add(l1);
        zadania.add(l2);
        while(!zadania.isEmpty())
        {
            System.out.println(zadania.poll().getCos());
        }
        SortedMap<String, String> ucz = new TreeMap<>();
        ucz.put("damian","chuj");
        ucz.put("damiadn","chudj");
        ucz.put("damisan","ccxhuj");
        ucz.remove("damisan");
        ucz.put("kozak","kamil");
        ucz.replace("damiadn","niechuj");
        Set<Entry<String,String>> entrySet = ucz.entrySet();
        for(Entry<String,String> entry: entrySet){
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }

        Stack<Integer> x = new Stack();
        x.push(3);
        x.push(2);
        x.push(5);
        x.push(1);
        System.out.println(x);
        System.out.println(x.pop());
        System.out.println(x.search(1));
        System.out.println(x.peek());

        LinkedList<String> lista = new LinkedList<String>();
        lista.add("lo");
        lista.add("lopez");
        lista.add("jenifer");
        System.out.println(lista);
        System.out.println(lista.getFirst());
        System.out.println(lista.getLast());

        ArrayList<String> y = new ArrayList<String>();
        y.add("pu");
        y.add("sia");
        y.add("sias");
        y.add("siad");
        y.set(3,"chuj");
        Collections.sort(y);
        System.out.println(y);
        System.out.println(y.get(1));
        System.out.println(y.size());

        Map<Integer,String> dic = new TreeMap<>();
        dic.put(3,"siema");
        dic.put(2,"sisema");
        dic.put(1,"siemda");
        System.out.println(dic);
        System.out.println(dic.size());
        Set<Integer> keySet = dic.keySet();
        System.out.println(keySet);
        Collection<String> val = dic.values();
        System.out.println(val);

        //wypis ladny calego jest na gorze

    }
}
    class ListComparator implements Comparator<List>
    {
        public int compare(List l1,List l2)
        {
            if(l1.n < l2.n)
                return -1;
            else if(l1.n > l2.n)
                return 1;
            return 0;
        }
    }
    class List
    {
        public String cos;
        public int n;
        public List(String cos,int n)
        {
            this.cos=cos;
            this.n=n;
        }
        public String getCos()
        {
            return cos;
        }
    }

