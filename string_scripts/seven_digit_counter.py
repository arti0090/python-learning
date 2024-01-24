segments = {
    '0': ['###', '# #', '# #', '# #', '###'],
    '1': ['  #', '  #', '  #', '  #', '  #'],
    '2': ['###', '  #', '###', '#  ', '###'],
    '3': ['###', '  #', '###', '  #', '###'],
    '4': ['# #', '# #', '###', '  #', '  #'],
    '5': ['###', '#  ', '###', '  #', '###'],
    '6': ['###', '#  ', '###', '# #', '###'],
    '7': ['###', '  #', '  #', '  #', '  #'],
    '8': ['###', '# #', '###', '# #', '###'],
    '9': ['###', '# #', '###', '  #', '###']
}

def display_number(number):
    lines = ['' for _ in range(5)]
    
    for digit in str(number):
        if digit in segments:
            digit_segments = segments[digit]
            
            for i, segment in enumerate(digit_segments):
                lines[i] += segment + ' '
                
    for line in lines:
        print(line)
        
display_number(123)