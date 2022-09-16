if 'option' in group_name:
                    option = self.__format_desc(specification, 'op')
                    if option not in spec['options']:
                        spec['options'].append(option)
                elif 'feature' in group_name:
                    spec['features'].append(self.__format_desc(specification, 'op'))
                elif 'engine' in group_name or 'power unit' in group_name:
                    spec['engine'][self.__convert_to_camel_case(specification['spec_name'])] = {'label': specification['spec_name'],
                                                                              'desc': self.__format_desc(specification)}
                elif 'dimension' in group_name or 'capacities' in group_name:
                    spec['dimensions'][self.__convert_to_camel_case(specification['spec_name'])] = {'label': specification['spec_name'],
                                                                                  'desc': self.__format_desc(specification)}
                elif 'transmission system' in group_name or 'clutch' in group_name or 'drive system' in group_name:
                    spec['drivetrain'][self.__convert_to_camel_case(specification['spec_name'])] = {'label': specification['spec_name'],
                                                                                  'desc': self.__format_desc(specification)}
                elif 'electrical' in group_name or 'mill motor' in group_name:
                    spec['electrical'][self.__convert_to_camel_case(specification['spec_name'])] = {'label': specification['spec_name'],
                                                                                  'desc': self.__format_desc(specification)}
                else:
                    spec['operational'][self.__convert_to_camel_case(specification['spec_name'])] = {'label': specification['spec_name'],
                                                                                   'desc': self.__format_desc(specification)}