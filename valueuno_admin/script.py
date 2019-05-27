from .models import NextDay

class NextDayPridictor:
    def fun(daysToRead):
        data = NextDay.objects.all()
        second_column = []
        third_column = []
        simple_cluster = []
        cluster = []
        dates_column = []
        dates_simple_cluster = []
        dates_cluster = []
        answer = []
        final_answer = []
        simple_cluster = []
        cluster = []
        data_value = []
        daysToReadInt = int(daysToRead)
        # second_column = data.col_values(3) simple_cluster

        # third_column = sheet.col_values(4) detailed cluster

        # dates_column = sheet.col_values(1) date

        # simple_cluster = second_column[-(daysToReadInt):]

        cluster = third_column[-(daysToReadInt):]

        if daysToReadInt == 2:
            context = {}
            for i in range(len(data) - (1 + daysToReadInt)):
                if ((data[i].simple_cluster == data[len(data)-2].simple_cluster) and (data[i+1].simple_cluster == data[len(data)-1].simple_cluster)):
                    dates_simple_cluster.append(data[i+2].date)
                    answer.append(data[i+2].simple_cluster)
                    data_value.append(data[i+2].open_value)
            context = dict(zip(dates_simple_cluster,answer))
            print("questioned: ", data[len(data)-1].date)
            return context
        elif daysToReadInt == 3:
            context = {}
            for i in range(len(data) - (1 + daysToReadInt)):
                if ((data[i].simple_cluster == data[len(data)-3].simple_cluster) and (data[i+1].simple_cluster == data[len(data)-2].simple_cluster) and (data[i+2].simple_cluster == data[len(data)-1].simple_cluster)):
                    dates_simple_cluster.append(data[i+3].date)
                    answer.append(data[i+3].simple_cluster)
                    data_value.append(data[i+3].open_value)
            context = dict(zip(dates_simple_cluster,answer))
            print("questioned: ", data[len(data)-1].date)
            return context
        elif daysToReadInt == 4:
            context = {}
            for i in range(len(data) - (1 + daysToReadInt)):
                if ((data[i].simple_cluster == data[len(data)-4].simple_cluster) and (data[i+1].simple_cluster == data[len(data)-3].simple_cluster) and (data[i+2].simple_cluster == data[len(data)-2].simple_cluster) and (data[i+3].simple_cluster == data[len(data)-1].simple_cluster)):
                    dates_simple_cluster.append(data[i+4].date)
                    answer.append(data[i+4].simple_cluster)
                    data_value.append(data[i+4].open_value)
            context = dict(zip(dates_simple_cluster,answer))
            print("questioned: ", data[len(data)-1].date)
            return context
        else:
            context = {}
            for i in range(len(data) - (1 + daysToReadInt)):
                if ((data[i].simple_cluster == data[len(data)-5].simple_cluster) and (data[i+1].simple_cluster == data[len(data)-4].simple_cluster) and (data[i+2].simple_cluster == data[len(data)-3].simple_cluster) and (data[i+3].simple_cluster == data[len(data)-2].simple_cluster) and (data[i+4].simple_cluster == data[len(data)-1].simple_cluster)):
                    dates_simple_cluster.append(data[i+5].date)
                    answer.append(data[i+5].simple_cluster)
                    data_value.append(data[i+5].open_value)
            print("questioned: ", data[len(data)-1].date)
            context = dict(zip(dates_simple_cluster,answer))
            return context
