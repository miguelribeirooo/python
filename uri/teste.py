hora_i = input().split()
hi, mi, si = int(hora_i[0]), int(hora_i[2]), int(hora_i[4])

minuto_seg = 60
hora_seg = minuto_seg * 60
dia_seg = hora_seg * 24
i = si + mi*minuto_seg + hi*hora_seg + di*dia_seg