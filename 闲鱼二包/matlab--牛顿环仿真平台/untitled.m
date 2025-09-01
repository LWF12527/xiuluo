function varargout = untitled(varargin)
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @untitled_OpeningFcn, ...
                   'gui_OutputFcn',  @untitled_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end
if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
function untitled_OpeningFcn(hObject, eventdata, handles, varargin)
handles.output = hObject;
guidata(hObject, handles);
function varargout = untitled_OutputFcn(hObject, eventdata, handles) 
varargout{1} = handles.output;
function edit1_Callback(hObject, eventdata, handles)
function edit1_CreateFcn(hObject, eventdata, handles)
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end
function edit2_Callback(hObject, eventdata, handles)
function edit2_CreateFcn(hObject, eventdata, handles)
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end
function edit3_Callback(hObject, eventdata, handles)
function edit3_CreateFcn(hObject, eventdata, handles)
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end
function edit4_Callback(hObject, eventdata, handles)
function edit4_CreateFcn(hObject, eventdata, handles)
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end
function pushbutton1_Callback(hObject, eventdata, handles)
rm=2; %�����λ���߳���һ�루mm��
temp = linspace(-rm, rm, 100);
[X, Y] = meshgrid(temp);           %�������ڻ��ƶ�άͼ��ľ���
Lambda=str2double(get(handles.edit1,'String'))*1e-6;                   %����Ⲩ����mm��
R=str2double(get(handles.edit2,'String'))*1e+3;                        %ƽ͹͸���İ뾶��mm��
d = (X.^2 + Y.^2)./(2 * R)+str2double(get(handles.edit3,'String'))*1e-6;        %���������Ĥ���
n = str2double(get(handles.edit4,'String'));                           %����������
Delte=2*n*d/Lambda*2*pi+pi;        %������λ��
I = 128*(cos(Delte/2)).^2;        %������Թ�ǿ
axes(handles.axes1)
image(I);
colormap gray
axis off
axis equal
title('ţ�ٻ�(Newton ring)','FontSize',12);
function pushbutton2_Callback(hObject, eventdata, handles)
rm=2; %�����λ���߳���һ�루mm��
temp = linspace(-rm, rm, 100);
[X, Y] = meshgrid(temp);           %�������ڻ��ƶ�άͼ��ľ���
Lambda=str2double(get(handles.edit1,'String'))*1e-6;                     %����Ⲩ����mm��
R=str2double(get(handles.edit2,'String'))*1e+3;                          %ƽ͹͸���İ뾶��mm��
d = (X.^2 + Y.^2)./(2 * R)+str2double(get(handles.edit3,'String'))*1e-6; %���������Ĥ���
n = str2double(get(handles.edit4,'String'));                             %����������
Delte=2*n*d/Lambda*2*pi+pi;        %������λ��
I = 128*(cos(Delte/2)).^2;      %������Թ�ǿ
axes(handles.axes1)
mesh(X,Y,I)
title('��ǿ�ֲ�','FontSize',12);
function pushbutton3_Callback(hObject, eventdata, handles)
close(gcf)

