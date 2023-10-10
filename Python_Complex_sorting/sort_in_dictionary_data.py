class HomePageData2(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        file_path = r'D:\Helpabode\Data\home1.json'

        try:
            with open(file_path, 'r') as file:
                data = file.read()
                jsonData = json.loads(data)
                results = []
                print("Json data", jsonData)
                print("\n")

                for key, category_data in jsonData.items():
                    print(key, ":-", category_data)

                    rank = category_data.get("rank", 0)
                    selected_controls = category_data.get("selectedControls", [])
                    print("Selected control", selected_controls)
                    text_ids = [control.get("textId") for control in selected_controls]

                    # Use Django ORM to fetch data from the 'Category' model
                    categories = Category.objects.filter(textId__in=text_ids)
                    
                    alldata = {}
                    for category in categories:
                        print("Riyad ...",category.textId )
                        alldata[category.textId] = {
                            "id": category.id,
                            "rank1": next((control.get("rank1") for control in selected_controls if control.get("textId") == category.textId), 0),
                            "textId": category.textId,
                            "title": category.title,
                            "image": f"/media/{str(category.image)}"
                        }

                    results.append({
                        "rank": rank,
                        key: alldata
                    })
                
                # Sort the results based on "rank"
                sorted_data = sorted(results, key=lambda x: x.get("rank"))
                
                # Sort the inner dictionaries based on "rank1"
                for result in sorted_data:
                    for key, value in result.items():
                        if isinstance(value, dict):
                            sorted_value = dict(sorted(value.items(), key=lambda x: x[1].get("rank1")))
                            result[key] = sorted_value
                            
                return Response({"results": sorted_data}, status=status.HTTP_200_OK)

        except FileNotFoundError:
            print(f"The file {file_path} does not exist.")
            return Response({"error": "File not found"}, status=status.HTTP_404_NOT_FOUND)       

