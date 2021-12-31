import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

class FindDuplicateFileInSystem {
    public List<List<String>> findDuplicate(String[] paths) {
        List<List<String>> result = new ArrayList<>();
        ArrayList<String> tempList;
        HashMap<String, ArrayList<String>> history = new HashMap<>();

        for(String path: paths) {
            String[] elements = path.split(" ");
            String directoryPath = elements[0];

            for(int i = 1; i < elements.length; i++) {
                String[] filenameContent = elements[i].split("\\(");
                String filename = filenameContent[0];
                String fileContent = filenameContent[1].substring(0, filenameContent[1].length() - 1);

                tempList = history.getOrDefault(fileContent, new ArrayList<>());
                tempList.add(directoryPath + "/" + filename);
                history.put(fileContent, tempList);

            }
        }

        for(String key: history.keySet()) {
            if(history.get(key).size() > 1) {
                result.add(history.get(key));
            }
        }

        return result;
    }

    public static void main(String[] args) {
        FindDuplicateFileInSystem fdfis = new FindDuplicateFileInSystem();
        List<String> arrayList = new ArrayList<>();
        arrayList.add("root/a 1.txt(abcd) 2.txt(efgh)");
        arrayList.add("root/c 3.txt(abcd)");
        arrayList.add("root/c/d 4.txt(efgh)");
        arrayList.add("root 4.txt(efgh)");
        System.out.println(fdfis.findDuplicate(arrayList.stream().toArray(String[]::new)));
    }
}